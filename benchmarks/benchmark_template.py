"""
Simple benchmark template generator.

Usage in benchmark file:
    from triplets_adapter import TripletsAdapter
    from benchmark_template import create_benchmarks

    create_benchmarks(
        adapter=TripletsAdapter(),
        dataset_key="svedala_igm_cgmes_3",
        parser_name="triplets",
        dataset_name="svedala"
    )
"""

import psutil
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from datasets import DATASETS, get_size_mb


def get_memory_mb():
    """Get current memory usage in MB."""
    return psutil.Process().memory_info().rss / 1024 / 1024


def create_benchmarks(adapter, dataset_key, parser_name, dataset_name):
    """
    Create all benchmark fixtures and tests for a parser+dataset.

    Call this from your benchmark file and it will inject all tests
    into the module's namespace.

    Args:
        adapter: ParserAdapter instance
        dataset_key: Key in DATASETS dict
        parser_name: Short name for parser (e.g., "triplets")
        dataset_name: Short name for dataset (e.g., "svedala")
    """

    # Get caller's globals to inject tests
    import inspect
    caller_globals = inspect.currentframe().f_back.f_globals

    # Memory baseline fixture
    @pytest.fixture(scope="module")
    def memory_baseline():
        return get_memory_mb()

    # Loaded object fixture
    @pytest.fixture(scope="module")
    def loaded_object():
        obj = adapter.load(dataset_key)
        yield obj
        # Cleanup if adapter has cleanup method
        if hasattr(adapter, 'cleanup'):
            adapter.cleanup()

    # Load test
    def test_load(benchmark, memory_baseline):
        """Benchmark loading dataset."""
        loaded_obj = benchmark(adapter.load, dataset_key)

        memory_delta = get_memory_mb() - memory_baseline
        metrics = adapter.get_load_metrics(loaded_obj, memory_delta)

        # Add dataset size
        dataset = DATASETS[dataset_key]
        if "ZIP" in dataset:
            size_mb = dataset["_metadata"]["size_mb"]
            metrics["dataset_size_mb"] = f"{size_mb:.1f}"
        else:
            files = [v for k, v in dataset.items() if k != "_metadata"]
            metrics["total_size_mb"] = f"{get_size_mb(files):.1f}"

        # Add library and dataset metadata
        metrics["library"] = parser_name
        metrics["dataset"] = dataset_name

        for key, value in metrics.items():
            benchmark.extra_info[key] = value

        # Cleanup if needed
        if hasattr(adapter, 'cleanup'):
            adapter.cleanup()

        assert loaded_obj is not None

    # Query tests
    def test_get_lines(benchmark, loaded_object):
        """Benchmark querying lines."""
        count = benchmark(adapter.get_lines_count, loaded_object)
        benchmark.extra_info["line_count"] = count
        benchmark.extra_info["query_type"] = "get_lines"
        benchmark.extra_info["library"] = parser_name
        benchmark.extra_info["dataset"] = dataset_name
        assert count > 0

    def test_get_generators(benchmark, loaded_object):
        """Benchmark querying generators."""
        count = benchmark(adapter.get_generators_count, loaded_object)
        benchmark.extra_info["generator_count"] = count
        benchmark.extra_info["query_type"] = "get_generators"
        benchmark.extra_info["library"] = parser_name
        benchmark.extra_info["dataset"] = dataset_name
        assert count > 0

    def test_get_loads(benchmark, loaded_object):
        """Benchmark querying loads."""
        count = benchmark(adapter.get_loads_count, loaded_object)
        benchmark.extra_info["load_count"] = count
        benchmark.extra_info["query_type"] = "get_loads"
        benchmark.extra_info["library"] = parser_name
        benchmark.extra_info["dataset"] = dataset_name
        # RealGrid has 0 loads, so allow >= 0
        assert count >= 0

    def test_get_substations(benchmark, loaded_object):
        """Benchmark querying substations."""
        count = benchmark(adapter.get_substations_count, loaded_object)
        benchmark.extra_info["substation_count"] = count
        benchmark.extra_info["query_type"] = "get_substations"
        benchmark.extra_info["library"] = parser_name
        benchmark.extra_info["dataset"] = dataset_name
        assert count > 0

    # Set proper test names for pytest discovery
    test_load.__name__ = f"test_{parser_name}_load_{dataset_name}"
    test_get_lines.__name__ = f"test_{parser_name}_get_lines"
    test_get_generators.__name__ = f"test_{parser_name}_get_generators"
    test_get_loads.__name__ = f"test_{parser_name}_get_loads"
    test_get_substations.__name__ = f"test_{parser_name}_get_substations"

    # Inject into caller's module namespace
    caller_globals['memory_baseline'] = memory_baseline
    caller_globals['loaded_object'] = loaded_object
    caller_globals[test_load.__name__] = test_load
    caller_globals[test_get_lines.__name__] = test_get_lines
    caller_globals[test_get_generators.__name__] = test_get_generators
    caller_globals[test_get_loads.__name__] = test_get_loads
    caller_globals[test_get_substations.__name__] = test_get_substations
