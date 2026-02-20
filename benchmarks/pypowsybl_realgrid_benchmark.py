"""
Benchmark for pypowsybl - RealGrid large dataset.

Tests loading performance using RealGrid CGMES 2.4.15 (~86 MB uncompressed).
"""

import os
import psutil
import pytest
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
def realgrid_zip():
    """RealGrid ZIP - large CGMES 2.4.15 test configuration."""
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
def loaded_network(realgrid_zip):
    """Load RealGrid network once for all query tests."""
    return pn.load(str(realgrid_zip))


def test_pypowsybl_load_realgrid(benchmark, realgrid_zip, memory_baseline):
    """Benchmark loading large RealGrid network."""

    def load_network():
        return pn.load(str(realgrid_zip))

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

    # Get dataset size from metadata (uncompressed size)
    dataset = DATASETS["realgrid_cgmes_2_4"]
    dataset_size_mb = dataset["_metadata"]["size_mb"]

    # Report metrics
    benchmark.extra_info["memory_mb"] = f"{memory_used:.1f}"
    benchmark.extra_info["dataset_size_mb"] = f"{dataset_size_mb:.1f}"
    benchmark.extra_info["buses"] = bus_count
    benchmark.extra_info["lines"] = total_lines
    benchmark.extra_info["ac_lines"] = line_count
    benchmark.extra_info["dangling_lines"] = dangling_line_count
    benchmark.extra_info["generators"] = generator_count
    benchmark.extra_info["loads"] = load_count
    benchmark.extra_info["substations"] = substation_count

    assert network is not None
    assert bus_count > 0


def test_pypowsybl_get_lines_realgrid(benchmark, loaded_network):
    """Benchmark retrieving line data from large network."""

    def get_lines():
        return loaded_network.get_lines()

    # Benchmark the query
    lines = benchmark(get_lines)

    benchmark.extra_info["line_count"] = len(lines)
    benchmark.extra_info["query_type"] = "get_lines"

    assert len(lines) > 0


def test_pypowsybl_get_generators_realgrid(benchmark, loaded_network):
    """Benchmark retrieving generator data from large network."""

    def get_generators():
        return loaded_network.get_generators()

    # Benchmark the query
    generators = benchmark(get_generators)

    benchmark.extra_info["generator_count"] = len(generators)
    benchmark.extra_info["query_type"] = "get_generators"

    assert len(generators) > 0


def test_pypowsybl_get_loads_realgrid(benchmark, loaded_network):
    """Benchmark retrieving load data from large network."""

    def get_loads():
        return loaded_network.get_loads()

    # Benchmark the query
    loads = benchmark(get_loads)

    benchmark.extra_info["load_count"] = len(loads)
    benchmark.extra_info["query_type"] = "get_loads"

    assert len(loads) > 0


def test_pypowsybl_get_substations_realgrid(benchmark, loaded_network):
    """Benchmark retrieving substation data from large network."""

    def get_substations():
        return loaded_network.get_substations()

    # Benchmark the query
    substations = benchmark(get_substations)

    benchmark.extra_info["substation_count"] = len(substations)
    benchmark.extra_info["query_type"] = "get_substations"

    assert len(substations) > 0
