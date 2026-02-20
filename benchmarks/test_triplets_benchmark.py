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
    from triplets.rdf_parser import load_RDF_to_dataframe, type_tableview
except ImportError:
    pytest.skip("triplets not available", allow_module_level=True)

# Import dataset definitions
from datasets import DATASETS, get_size_mb


@pytest.fixture(scope="module")
def svedala_files():
    """Path to Svedala IGM dataset files."""
    dataset = DATASETS["svedala_igm_cgmes_3"]
    files = {k: v for k, v in dataset.items() if k != "COMMON"}

    # Check if files exist
    for profile, path in files.items():
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


def test_triplets_load_eq_only(benchmark, svedala_files, memory_baseline):
    """Benchmark loading only Equipment profile (largest file)."""

    def load_eq():
        df = load_RDF_to_dataframe(str(svedala_files["EQ"]))
        return df

    # Run benchmark
    df = benchmark(load_eq)

    # Collect metrics
    memory_used = get_memory_mb() - memory_baseline

    # Get object counts - DataFrame has columns: [ID, KEY, VALUE, INSTANCE_ID]
    triplet_count = len(df)
    unique_objects = df['ID'].nunique()

    # Report metrics in benchmark extra_info
    benchmark.extra_info["memory_mb"] = f"{memory_used:.1f}"
    benchmark.extra_info["triplets_count"] = triplet_count
    benchmark.extra_info["unique_objects"] = unique_objects
    benchmark.extra_info["file_size_mb"] = f"{get_size_mb([svedala_files['EQ']]):.1f}"

    assert df is not None
    assert len(df) > 0


def test_triplets_load_full_model(benchmark, svedala_files, memory_baseline):
    """Benchmark loading complete CGMES model (EQ + SSH + SV + TP)."""

    def load_full():
        # Load all profiles - concatenate DataFrames
        dfs = []
        for file_path in svedala_files.values():
            df = load_RDF_to_dataframe(str(file_path))
            dfs.append(df)
        return pandas.concat(dfs, ignore_index=True)

    # Run benchmark
    df = benchmark(load_full)

    # Collect metrics
    memory_used = get_memory_mb() - memory_baseline
    triplet_count = len(df)
    unique_objects = df['ID'].nunique()
    instances = df['INSTANCE_ID'].nunique()

    # Get network statistics (matching pypowsybl metrics)
    line_count = df.query("KEY == 'Type' & VALUE == 'ACLineSegment'")["ID"].nunique()
    generator_count = df.query("KEY == 'Type' & VALUE == 'SynchronousMachine'")["ID"].nunique()
    load_count = (df.query("KEY == 'Type' & VALUE == 'ConformLoad'")["ID"].nunique() +
                  df.query("KEY == 'Type' & VALUE == 'NonConformLoad'")["ID"].nunique())
    substation_count = df.query("KEY == 'Type' & VALUE == 'Substation'")["ID"].nunique()

    # Calculate total file size
    total_size_mb = get_size_mb(list(svedala_files.values()))

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

    assert df is not None
    assert len(df) > 0


def test_triplets_query_performance(benchmark, svedala_files):
    """Benchmark querying loaded data using type_tableview."""

    # Load data first (not benchmarked)
    df = load_RDF_to_dataframe(str(svedala_files["EQ"]))

    def query_acline_segments():
        # Query for ACLineSegment objects using type_tableview
        results = type_tableview(df, "ACLineSegment")
        return results

    # Benchmark the query
    results = benchmark(query_acline_segments)

    benchmark.extra_info["results_count"] = len(results)
    benchmark.extra_info["query_type"] = "ACLineSegment"

    assert len(results) > 0
