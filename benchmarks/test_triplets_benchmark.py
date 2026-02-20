"""
Benchmark for triplets library - CIM RDF parser.

Tests loading performance using the Svedala IGM dataset (7.3MB total).
"""

import os
import psutil
import pytest
from pathlib import Path
import sys

# Add parsers directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

# Import triplets
try:
    import pandas
except ImportError:
    pytest.skip("triplets not available", allow_module_level=True)

# Import dataset definitions and parsers
from datasets import DATASETS, get_size_mb
from triplets_loader import TripletsLoader


@pytest.fixture(scope="module")
def svedala_files():
    """Path to Svedala IGM dataset files including COMMON."""
    dataset = DATASETS["svedala_igm_cgmes_3"]
    files = list(dataset.values())

    # Check if files exist
    for path in files:
        if not path.exists():
            pytest.skip(f"Test data not available: {path}")

    return files


@pytest.fixture(scope="module")
def memory_baseline():
    """Get baseline memory usage."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # MB


def get_memory_mb():
    """Get current memory usage in MB."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024


@pytest.fixture(scope="module")
def loaded_loader(svedala_files):
    """Load full CGMES model once for all query tests."""
    loader = TripletsLoader()
    loader.load_files([str(f) for f in svedala_files])
    return loader


def test_triplets_load_full_model(benchmark, svedala_files, memory_baseline):
    """Benchmark loading complete CGMES model (EQ + SSH + SV + TP + COMMON)."""

    def load_full():
        loader = TripletsLoader()
        loader.load_files([str(f) for f in svedala_files])
        return loader

    # Run benchmark
    loader = benchmark(load_full)

    # Collect metrics
    memory_used = get_memory_mb() - memory_baseline
    triplet_count = len(loader.df)
    unique_objects = loader.df['ID'].nunique()
    instances = loader.df['INSTANCE_ID'].nunique()

    # Get network statistics using loader methods
    line_count = loader.get_lines()
    generator_count = loader.get_generators()
    load_count = loader.get_loads()
    substation_count = loader.get_substations()

    # Calculate total file size
    total_size_mb = get_size_mb(svedala_files)

    # Report metrics
    benchmark.extra_info["memory_mb"] = f"{memory_used:.1f}"
    benchmark.extra_info["triplets_count"] = triplet_count
    benchmark.extra_info["unique_objects"] = unique_objects
    benchmark.extra_info["instances"] = instances
    benchmark.extra_info["total_size_mb"] = f"{total_size_mb:.1f}"
    benchmark.extra_info["files_loaded"] = len(svedala_files)
    benchmark.extra_info["lines"] = line_count
    benchmark.extra_info["generators"] = generator_count
    benchmark.extra_info["loads"] = load_count
    benchmark.extra_info["substations"] = substation_count

    assert loader.df is not None
    assert len(loader.df) > 0


def test_triplets_get_lines(benchmark, loaded_loader):
    """Benchmark querying ACLineSegment objects."""

    # Benchmark the query using loader method
    line_count = benchmark(loaded_loader.get_lines)

    benchmark.extra_info["line_count"] = line_count
    benchmark.extra_info["query_type"] = "get_lines"

    assert line_count > 0


def test_triplets_get_generators(benchmark, loaded_loader):
    """Benchmark querying SynchronousMachine objects."""

    # Benchmark the query using loader method
    gen_count = benchmark(loaded_loader.get_generators)

    benchmark.extra_info["generator_count"] = gen_count
    benchmark.extra_info["query_type"] = "get_generators"

    assert gen_count > 0


def test_triplets_get_loads(benchmark, loaded_loader):
    """Benchmark querying ConformLoad and NonConformLoad objects."""

    # Benchmark the query using loader method
    load_count = benchmark(loaded_loader.get_loads)

    benchmark.extra_info["load_count"] = load_count
    benchmark.extra_info["query_type"] = "get_loads"

    assert load_count > 0


def test_triplets_get_substations(benchmark, loaded_loader):
    """Benchmark querying Substation objects."""

    # Benchmark the query using loader method
    substation_count = benchmark(loaded_loader.get_substations)

    benchmark.extra_info["substation_count"] = substation_count
    benchmark.extra_info["query_type"] = "get_substations"

    assert substation_count > 0
