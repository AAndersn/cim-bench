#!/usr/bin/env python
"""
Generate loading speed comparison graphs from benchmark results.

Groups results by dataset (Svedala, RealGrid) and compares tools side-by-side.

Usage:
    python tools/generate_graphs.py
"""

import json
import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pathlib import Path

# Use non-interactive backend for server environments
matplotlib.use('Agg')


def extract_benchmark_data(benchmark_json):
    """Extract load and query benchmark data from JSON."""
    with open(benchmark_json) as f:
        data = json.load(f)

    load_data = None
    query_data = {}

    for bench in data["benchmarks"]:
        name = bench["name"]

        # Extract load benchmark (no get_ prefix)
        if "load" in name.lower() and "get_" not in name.lower():
            load_data = {
                "name": name,
                "mean": bench["stats"]["mean"],
                "stddev": bench["stats"]["stddev"],
                "extra": bench.get("extra_info", {})
            }

        # Extract query benchmarks
        elif "get_" in name.lower():
            query_type = name.split("get_")[-1].replace("_", " ").title()
            query_data[query_type] = {
                "mean": bench["stats"]["mean"],
                "extra": bench.get("extra_info", {})
            }

    return load_data, query_data


def generate_dataset_comparison(dataset_name, triplets_file, pypowsybl_file, output_path):
    """Generate comparison chart for a single dataset showing both tools."""

    # Extract data for both tools
    triplets_load, triplets_queries = extract_benchmark_data(triplets_file)
    pypowsybl_load, pypowsybl_queries = extract_benchmark_data(pypowsybl_file)

    if not triplets_load or not pypowsybl_load:
        print(f"⚠️  Incomplete data for {dataset_name}")
        return

    # Create figure with 3 subplots: Load Time, Memory, Query Performance
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    tools = ['Triplets', 'PyPowSyBl']
    colors = ['#3498db', '#e74c3c']

    # Chart 1: Load Time Comparison
    load_times = [
        triplets_load["mean"] * 1000,  # Convert to ms
        pypowsybl_load["mean"] * 1000
    ]
    bars1 = ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (ms)', fontsize=11)
    ax1.set_title(f'{dataset_name} - Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar, val in zip(bars1, load_times):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f} ms',
                ha='center', va='bottom', fontsize=9)

    # Chart 2: Memory Usage Comparison
    memory = [
        float(triplets_load["extra"].get("memory_mb", 0)),
        float(pypowsybl_load["extra"].get("memory_mb", 0))
    ]
    bars2 = ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title(f'{dataset_name} - Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar, val in zip(bars2, memory):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f} MB',
                ha='center', va='bottom', fontsize=9)

    # Chart 3: Query Performance Comparison (average of all queries)
    # Get common query types
    triplets_avg = np.mean([q["mean"] * 1000 for q in triplets_queries.values()])
    pypowsybl_avg = np.mean([q["mean"] * 1000 for q in pypowsybl_queries.values()])

    query_times = [triplets_avg, pypowsybl_avg]
    bars3 = ax3.bar(tools, query_times, color=colors)
    ax3.set_ylabel('Average Query Time (ms)', fontsize=11)
    ax3.set_title(f'{dataset_name} - Query Performance', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar, val in zip(bars3, query_times):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.2f} ms',
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path}")


def generate_detailed_comparison(dataset_name, triplets_file, pypowsybl_file, output_path):
    """Generate detailed comparison with network elements parsed."""

    # Extract data for both tools
    triplets_load, _ = extract_benchmark_data(triplets_file)
    pypowsybl_load, _ = extract_benchmark_data(pypowsybl_file)

    if not triplets_load or not pypowsybl_load:
        print(f"⚠️  Incomplete data for {dataset_name}")
        return

    # Create figure with 2x2 subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    tools = ['Triplets', 'PyPowSyBl']
    colors = ['#3498db', '#e74c3c']

    # Chart 1: Load Time
    load_times = [
        triplets_load["mean"] * 1000,
        pypowsybl_load["mean"] * 1000
    ]
    bars1 = ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (ms)', fontsize=11)
    ax1.set_title('Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    for bar, val in zip(bars1, load_times):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f}', ha='center', va='bottom', fontsize=9)

    # Chart 2: Memory Usage
    memory = [
        float(triplets_load["extra"].get("memory_mb", 0)),
        float(pypowsybl_load["extra"].get("memory_mb", 0))
    ]
    bars2 = ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title('Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    for bar, val in zip(bars2, memory):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f}', ha='center', va='bottom', fontsize=9)

    # Chart 3: Lines Parsed
    lines = [
        int(triplets_load["extra"].get("lines", 0)),
        int(pypowsybl_load["extra"].get("lines", 0))
    ]
    bars3 = ax3.bar(tools, lines, color=colors)
    ax3.set_ylabel('Line Count', fontsize=11)
    ax3.set_title('Lines Parsed', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    for bar, val in zip(bars3, lines):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:,}', ha='center', va='bottom', fontsize=9)

    # Chart 4: Generators Parsed
    generators = [
        int(triplets_load["extra"].get("generators", 0)),
        int(pypowsybl_load["extra"].get("generators", 0))
    ]
    bars4 = ax4.bar(tools, generators, color=colors)
    ax4.set_ylabel('Generator Count', fontsize=11)
    ax4.set_title('Generators Parsed', fontsize=12, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)
    for bar, val in zip(bars4, generators):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:,}', ha='center', va='bottom', fontsize=9)

    plt.suptitle(f'{dataset_name} Dataset - Detailed Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path}")


def generate_import_comparison(output_path):
    """Generate chart comparing import/load times across datasets."""

    results_dir = Path("results")

    # Define benchmark files
    svedala_files = {
        "triplets": results_dir / "triplets_svedala_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_svedala_benchmark.json"
    }

    realgrid_files = {
        "triplets": results_dir / "triplets_realgrid_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_realgrid_benchmark.json"
    }

    # Check if all files exist
    if not all(f.exists() for f in list(svedala_files.values()) + list(realgrid_files.values())):
        print("⚠️  Missing benchmark files for import comparison")
        return

    # Extract data
    data = {}
    for tool in ["triplets", "pypowsybl"]:
        svedala_load, _ = extract_benchmark_data(svedala_files[tool])
        realgrid_load, _ = extract_benchmark_data(realgrid_files[tool])

        if svedala_load and realgrid_load:
            data[tool] = {
                "svedala": svedala_load["mean"] * 1000,
                "realgrid": realgrid_load["mean"] * 1000
            }

    if len(data) < 2:
        print("⚠️  Incomplete data for import comparison")
        return

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    datasets = ['Svedala\n(7.3 MB)', 'RealGrid\n(86.5 MB)']
    x = np.arange(len(datasets))
    width = 0.35

    triplets_times = [data["triplets"]["svedala"], data["triplets"]["realgrid"]]
    pypowsybl_times = [data["pypowsybl"]["svedala"], data["pypowsybl"]["realgrid"]]

    bars1 = ax.bar(x - width/2, triplets_times, width, label='Triplets', color='#3498db')
    bars2 = ax.bar(x + width/2, pypowsybl_times, width, label='PyPowSyBl', color='#e74c3c')

    ax.set_ylabel('Import Time (ms)', fontsize=12)
    ax.set_title('Import Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path}")


def generate_memory_comparison(output_path):
    """Generate chart comparing memory usage across datasets."""

    results_dir = Path("results")

    # Define benchmark files
    svedala_files = {
        "triplets": results_dir / "triplets_svedala_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_svedala_benchmark.json"
    }

    realgrid_files = {
        "triplets": results_dir / "triplets_realgrid_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_realgrid_benchmark.json"
    }

    # Check if all files exist
    if not all(f.exists() for f in list(svedala_files.values()) + list(realgrid_files.values())):
        print("⚠️  Missing benchmark files for memory comparison")
        return

    # Extract data
    data = {}
    for tool in ["triplets", "pypowsybl"]:
        svedala_load, _ = extract_benchmark_data(svedala_files[tool])
        realgrid_load, _ = extract_benchmark_data(realgrid_files[tool])

        if svedala_load and realgrid_load:
            data[tool] = {
                "svedala": float(svedala_load["extra"].get("memory_mb", 0)),
                "realgrid": float(realgrid_load["extra"].get("memory_mb", 0))
            }

    if len(data) < 2:
        print("⚠️  Incomplete data for memory comparison")
        return

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    datasets = ['Svedala\n(7.3 MB)', 'RealGrid\n(86.5 MB)']
    x = np.arange(len(datasets))
    width = 0.35

    triplets_memory = [data["triplets"]["svedala"], data["triplets"]["realgrid"]]
    pypowsybl_memory = [data["pypowsybl"]["svedala"], data["pypowsybl"]["realgrid"]]

    bars1 = ax.bar(x - width/2, triplets_memory, width, label='Triplets', color='#3498db')
    bars2 = ax.bar(x + width/2, pypowsybl_memory, width, label='PyPowSyBl', color='#e74c3c')

    ax.set_ylabel('Memory Usage (MB)', fontsize=12)
    ax.set_title('Memory Consumption Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path}")


def generate_query_comparison(output_path):
    """Generate chart comparing average query times across datasets."""

    results_dir = Path("results")

    # Define benchmark files
    svedala_files = {
        "triplets": results_dir / "triplets_svedala_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_svedala_benchmark.json"
    }

    realgrid_files = {
        "triplets": results_dir / "triplets_realgrid_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_realgrid_benchmark.json"
    }

    # Check if all files exist
    if not all(f.exists() for f in list(svedala_files.values()) + list(realgrid_files.values())):
        print("⚠️  Missing benchmark files for query comparison")
        return

    # Extract data
    data = {}
    for tool in ["triplets", "pypowsybl"]:
        svedala_load, svedala_queries = extract_benchmark_data(svedala_files[tool])
        realgrid_load, realgrid_queries = extract_benchmark_data(realgrid_files[tool])

        if svedala_queries and realgrid_queries:
            # Calculate average query time for each dataset
            svedala_avg = np.mean([q["mean"] * 1000 for q in svedala_queries.values()])
            realgrid_avg = np.mean([q["mean"] * 1000 for q in realgrid_queries.values()])

            data[tool] = {
                "svedala": svedala_avg,
                "realgrid": realgrid_avg
            }

    if len(data) < 2:
        print("⚠️  Incomplete data for query comparison")
        return

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    datasets = ['Svedala\n(7.3 MB)', 'RealGrid\n(86.5 MB)']
    x = np.arange(len(datasets))
    width = 0.35

    triplets_queries = [data["triplets"]["svedala"], data["triplets"]["realgrid"]]
    pypowsybl_queries = [data["pypowsybl"]["svedala"], data["pypowsybl"]["realgrid"]]

    bars1 = ax.bar(x - width/2, triplets_queries, width, label='Triplets', color='#3498db')
    bars2 = ax.bar(x + width/2, pypowsybl_queries, width, label='PyPowSyBl', color='#e74c3c')

    ax.set_ylabel('Average Query Time (ms)', fontsize=12)
    ax.set_title('Query Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, format='svg', bbox_inches='tight')
    print(f"   → {output_path}")


def main():
    """Generate all graphs from benchmark results in SVG format."""

    results_dir = Path("results")
    graphs_dir = results_dir / "graphs"
    graphs_dir.mkdir(exist_ok=True)

    # Define benchmark files
    svedala_files = {
        "triplets": results_dir / "triplets_svedala_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_svedala_benchmark.json"
    }

    realgrid_files = {
        "triplets": results_dir / "triplets_realgrid_benchmark.json",
        "pypowsybl": results_dir / "pypowsybl_realgrid_benchmark.json"
    }

    print("📊 Generating performance graphs...")

    # Generate Svedala dataset comparison
    if all(f.exists() for f in svedala_files.values()):
        print("   Svedala dataset:")
        generate_dataset_comparison(
            "Svedala",
            svedala_files["triplets"],
            svedala_files["pypowsybl"],
            graphs_dir / "svedala_comparison.svg"
        )
        generate_detailed_comparison(
            "Svedala",
            svedala_files["triplets"],
            svedala_files["pypowsybl"],
            graphs_dir / "svedala_detailed.svg"
        )

    # Generate RealGrid dataset comparison
    if all(f.exists() for f in realgrid_files.values()):
        print("   RealGrid dataset:")
        generate_dataset_comparison(
            "RealGrid",
            realgrid_files["triplets"],
            realgrid_files["pypowsybl"],
            graphs_dir / "realgrid_comparison.svg"
        )
        generate_detailed_comparison(
            "RealGrid",
            realgrid_files["triplets"],
            realgrid_files["pypowsybl"],
            graphs_dir / "realgrid_detailed.svg"
        )

    # Generate cross-dataset comparisons
    print("   Cross-dataset comparisons:")
    generate_import_comparison(graphs_dir / "import_comparison.svg")
    generate_memory_comparison(graphs_dir / "memory_comparison.svg")
    generate_query_comparison(graphs_dir / "query_comparison.svg")

    print("")
    print("✅ Graph generation complete!")
    print(f"   Location: {graphs_dir}/")


if __name__ == "__main__":
    try:
        import matplotlib
    except ImportError:
        print("❌ Error: matplotlib not installed")
        print("   Install with: pip install matplotlib")
        sys.exit(1)

    main()
