"""
Benchmark for pypowsybl library - Power system network modeling and analysis.

Tests loading performance using the Svedala IGM dataset (7.3MB total) with CommonData.
"""

import os
import psutil
import pytest
import tempfile
import zipfile
from pathlib import Path
import sys

# Add parsers directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

# Import pypowsybl
try:
    import pypowsybl.network as pn
except ImportError:
    pytest.skip("pypowsybl not available", allow_module_level=True)

# Import dataset definitions
from datasets import DATASETS, get_size_mb


@pytest.fixture(scope="module")
def svedala_zip_path():
    """Create a ZIP file with Svedala IGM dataset + CommonData for pypowsybl."""
    dataset = DATASETS["svedala_igm_cgmes_3"]

    # Get all files including common data, excluding metadata
    files = [v for k, v in dataset.items() if k != "_metadata"]

    # Check if files exist
    for f in files:
        if not f.exists():
            pytest.skip(f"Test data not available: {f}")

    # Create temporary ZIP file
    tmp_zip = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
    with zipfile.ZipFile(tmp_zip.name, "w") as zf:
        for f in files:
            zf.write(f, arcname=f.name)

    total_size_mb = get_size_mb(files)

    yield tmp_zip.name, total_size_mb

    # Cleanup
    os.unlink(tmp_zip.name)


@pytest.fixture(scope="module")
def memory_baseline():
    """Get baseline memory usage."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # MB


def get_memory_mb():
    """Get current memory usage in MB."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024


def test_pypowsybl_load_network(benchmark, svedala_zip_path, memory_baseline):
    """Benchmark loading complete CGMES network."""
    zip_path, total_size_mb = svedala_zip_path

    def load_network():
        network = pn.load(zip_path)
        return network

    # Run benchmark
    network = benchmark(load_network)

    # Collect metrics
    memory_used = get_memory_mb() - memory_baseline

    # Get network statistics
    bus_count = len(network.get_buses())
    line_count = len(network.get_lines())
    dangling_line_count = len(network.get_dangling_lines())
    total_lines = line_count + dangling_line_count
    generator_count = len(network.get_generators())
    load_count = len(network.get_loads())
    substation_count = len(network.get_substations())

    # Report metrics
    benchmark.extra_info["memory_mb"] = f"{memory_used:.1f}"
    benchmark.extra_info["total_size_mb"] = f"{total_size_mb:.1f}"
    benchmark.extra_info["buses"] = bus_count
    benchmark.extra_info["lines"] = total_lines
    benchmark.extra_info["ac_lines"] = line_count
    benchmark.extra_info["dangling_lines"] = dangling_line_count
    benchmark.extra_info["generators"] = generator_count
    benchmark.extra_info["loads"] = load_count
    benchmark.extra_info["substations"] = substation_count

    assert network is not None
    assert bus_count > 0


def test_pypowsybl_get_lines(benchmark, svedala_zip_path):
    """Benchmark retrieving line data from loaded network."""

    zip_path, _ = svedala_zip_path

    # Load network first (not benchmarked)
    network = pn.load(zip_path)

    def get_lines():
        lines_df = network.get_lines()
        return lines_df

    # Benchmark the query
    lines = benchmark(get_lines)

    benchmark.extra_info["line_count"] = len(lines)
    benchmark.extra_info["query_type"] = "get_lines"

    assert len(lines) > 0


def test_pypowsybl_get_generators(benchmark, svedala_zip_path):
    """Benchmark retrieving generator data from loaded network."""

    zip_path, _ = svedala_zip_path

    # Load network first (not benchmarked)
    network = pn.load(zip_path)

    def get_generators():
        gens_df = network.get_generators()
        return gens_df

    # Benchmark the query
    generators = benchmark(get_generators)

    benchmark.extra_info["generator_count"] = len(generators)
    benchmark.extra_info["query_type"] = "get_generators"

    assert len(generators) > 0


def test_pypowsybl_get_loads(benchmark, svedala_zip_path):
    """Benchmark retrieving load data from loaded network."""

    zip_path, _ = svedala_zip_path

    # Load network first (not benchmarked)
    network = pn.load(zip_path)

    def get_loads():
        return network.get_loads()

    # Benchmark the query
    loads = benchmark(get_loads)

    benchmark.extra_info["load_count"] = len(loads)
    benchmark.extra_info["query_type"] = "get_loads"

    assert len(loads) > 0


def test_pypowsybl_get_substations(benchmark, svedala_zip_path):
    """Benchmark retrieving substation data from loaded network."""

    zip_path, _ = svedala_zip_path

    # Load network first (not benchmarked)
    network = pn.load(zip_path)

    def get_substations():
        return network.get_substations()

    # Benchmark the query
    substations = benchmark(get_substations)

    benchmark.extra_info["substation_count"] = len(substations)
    benchmark.extra_info["query_type"] = "get_substations"

    assert len(substations) > 0
