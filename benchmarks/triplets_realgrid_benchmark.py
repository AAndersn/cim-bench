"""
Benchmark for triplets library - RealGrid large dataset.

Tests loading performance using RealGrid CGMES 2.4.15 (~86 MB uncompressed).
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
def realgrid_zip():
    """RealGrid ZIP path - large CGMES 2.4.15 test configuration."""
    dataset = DATASETS["realgrid_cgmes_2_4"]
    zip_path = dataset["ZIP"]
    if not zip_path.exists():
        pytest.skip(f"RealGrid test data not available: {zip_path}")
    return zip_path


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
def loaded_loader(realgrid_zip):
    """Load RealGrid once for all query tests."""
    loader = TripletsLoader()
    loader.load_zip(str(realgrid_zip))
    return loader


def test_triplets_load_realgrid(benchmark, realgrid_zip, memory_baseline):
    """Benchmark loading large RealGrid dataset."""

    def load_realgrid():
        loader = TripletsLoader()
        loader.load_zip(str(realgrid_zip))
        return loader

    # Run benchmark
    loader = benchmark(load_realgrid)

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

    # Get dataset size from metadata (uncompressed size)
    dataset = DATASETS["realgrid_cgmes_2_4"]
    dataset_size_mb = dataset["_metadata"]["size_mb"]

    # Report metrics
    benchmark.extra_info["memory_mb"] = f"{memory_used:.1f}"
    benchmark.extra_info["triplets_count"] = triplet_count
    benchmark.extra_info["unique_objects"] = unique_objects
    benchmark.extra_info["instances"] = instances
    benchmark.extra_info["dataset_size_mb"] = f"{dataset_size_mb:.1f}"
    benchmark.extra_info["lines"] = line_count
    benchmark.extra_info["generators"] = generator_count
    benchmark.extra_info["loads"] = load_count
    benchmark.extra_info["substations"] = substation_count

    assert loader.df is not None
    assert len(loader.df) > 0


def test_triplets_get_lines_realgrid(benchmark, loaded_loader):
    """Benchmark querying ACLineSegment objects on large dataset."""

    # Benchmark the query using loader method
    line_count = benchmark(loaded_loader.get_lines)

    benchmark.extra_info["line_count"] = line_count
    benchmark.extra_info["query_type"] = "get_lines"

    assert line_count > 0


def test_triplets_get_generators_realgrid(benchmark, loaded_loader):
    """Benchmark querying SynchronousMachine objects on large dataset."""

    # Benchmark the query using loader method
    gen_count = benchmark(loaded_loader.get_generators)

    benchmark.extra_info["generator_count"] = gen_count
    benchmark.extra_info["query_type"] = "get_generators"

    assert gen_count > 0


def test_triplets_get_loads_realgrid(benchmark, loaded_loader):
    """Benchmark querying ConformLoad and NonConformLoad objects on large dataset."""

    # Benchmark the query using loader method
    load_count = benchmark(loaded_loader.get_loads)

    benchmark.extra_info["load_count"] = load_count
    benchmark.extra_info["query_type"] = "get_loads"

    # RealGrid dataset has 0 loads, which is valid
    assert load_count >= 0


def test_triplets_get_substations_realgrid(benchmark, loaded_loader):
    """Benchmark querying Substation objects on large dataset."""

    # Benchmark the query using loader method
    substation_count = benchmark(loaded_loader.get_substations)

    benchmark.extra_info["substation_count"] = substation_count
    benchmark.extra_info["query_type"] = "get_substations"

    assert substation_count > 0
