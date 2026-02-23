#!/usr/bin/env python
"""Generate performance comparison graphs from benchmark results."""

import json
import sys
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pathlib import Path
from collections import defaultdict

matplotlib.use('Agg')


def load_benchmarks(results_dir):
    """Load all benchmark JSONs and organize by dataset."""
    data = defaultdict(lambda: defaultdict(dict))

    for json_file in Path(results_dir).glob("*_benchmark.json"):
        with open(json_file) as f:
            benchmarks = json.load(f)["benchmarks"]

        for bench in benchmarks:
            extra = bench.get("extra_info", {})
            if "dataset" not in extra or "display_name" not in extra:
                continue

            dataset = extra["dataset"]
            tool = extra["display_name"]

            if "load" in bench["name"].lower() and "get_" not in bench["name"].lower():
                data[dataset][tool]["load"] = {
                    "time": bench["stats"]["mean"] * 1000,
                    "memory": float(extra.get("memory_mb", 0)),
                    "lines": int(extra.get("lines", 0)),
                    "generators": int(extra.get("generators", 0)),
                    "color": extra.get("color", "#999999")
                }
            elif "get_" in bench["name"].lower():
                if "queries" not in data[dataset][tool]:
                    data[dataset][tool]["queries"] = []
                data[dataset][tool]["queries"].append(bench["stats"]["mean"] * 1000)
                data[dataset][tool]["color"] = extra.get("color", "#999999")

    return data


def plot_dataset(dataset_name, tools_data, output_dir):
    """Generate comparison and detailed charts for a dataset."""
    if len(tools_data) < 2:
        return

    tools = sorted(tools_data.keys())
    colors = [tools_data[t].get("color", "#999999") for t in tools]

    # Comparison chart
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    load_times = [tools_data[t]["load"]["time"] for t in tools]
    ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (ms)', fontsize=11)
    ax1.set_title(f'{dataset_name} - Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    for i, v in enumerate(load_times):
        ax1.text(i, v, f'{v:.1f} ms', ha='center', va='bottom', fontsize=9)

    memory = [tools_data[t]["load"]["memory"] for t in tools]
    ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title(f'{dataset_name} - Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    for i, v in enumerate(memory):
        ax2.text(i, v, f'{v:.1f} MB', ha='center', va='bottom', fontsize=9)

    query_times = [np.mean(tools_data[t].get("queries", [0])) for t in tools]
    ax3.bar(tools, query_times, color=colors)
    ax3.set_ylabel('Average Query Time (ms)', fontsize=11)
    ax3.set_title(f'{dataset_name} - Query Performance', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    for i, v in enumerate(query_times):
        ax3.text(i, v, f'{v:.2f} ms', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name.lower()}_comparison.svg", format='svg', bbox_inches='tight')
    print(f"   → {dataset_name.lower()}_comparison.svg")

    # Detailed chart
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    ax1.bar(tools, load_times, color=colors)
    ax1.set_ylabel('Load Time (ms)', fontsize=11)
    ax1.set_title('Loading Performance', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    for i, v in enumerate(load_times):
        ax1.text(i, v, f'{v:.1f}', ha='center', va='bottom', fontsize=9)

    ax2.bar(tools, memory, color=colors)
    ax2.set_ylabel('Memory (MB)', fontsize=11)
    ax2.set_title('Memory Consumption', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    for i, v in enumerate(memory):
        ax2.text(i, v, f'{v:.1f}', ha='center', va='bottom', fontsize=9)

    lines = [tools_data[t]["load"]["lines"] for t in tools]
    ax3.bar(tools, lines, color=colors)
    ax3.set_ylabel('Line Count', fontsize=11)
    ax3.set_title('Lines Parsed', fontsize=12, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    for i, v in enumerate(lines):
        ax3.text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=9)

    generators = [tools_data[t]["load"]["generators"] for t in tools]
    ax4.bar(tools, generators, color=colors)
    ax4.set_ylabel('Generator Count', fontsize=11)
    ax4.set_title('Generators Parsed', fontsize=12, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)
    for i, v in enumerate(generators):
        ax4.text(i, v, f'{v:,}', ha='center', va='bottom', fontsize=9)

    plt.suptitle(f'{dataset_name} Dataset - Detailed Comparison', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_dir / f"{dataset_name.lower()}_detailed.svg", format='svg', bbox_inches='tight')
    print(f"   → {dataset_name.lower()}_detailed.svg")


def plot_cross_dataset(data, output_dir):
    """Generate cross-dataset comparison charts."""
    datasets = sorted(data.keys())
    if len(datasets) < 2:
        return

    tools = sorted(set(t for ds in data.values() for t in ds.keys()))
    colors = {t: data[datasets[0]][t].get("color", "#999999") for t in tools if t in data[datasets[0]]}

    x = np.arange(len(datasets))
    width = 0.8 / len(tools)

    # Import comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, tool in enumerate(tools):
        times = [data[ds].get(tool, {}).get("load", {}).get("time", 0) for ds in datasets]
        offset = (i - len(tools)/2 + 0.5) * width
        bars = ax.bar(x + offset, times, width, label=tool, color=colors.get(tool, "#999999"))
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h, f'{h:.1f}', ha='center', va='bottom', fontsize=9)

    ax.set_ylabel('Import Time (ms)', fontsize=12)
    ax.set_title('Import Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'{ds.capitalize()}\n(7.3 MB)' if ds == 'svedala' else f'{ds.capitalize()}\n(86.5 MB)' for ds in datasets])
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "import_comparison.svg", format='svg', bbox_inches='tight')
    print("   → import_comparison.svg")

    # Memory comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, tool in enumerate(tools):
        memory = [data[ds].get(tool, {}).get("load", {}).get("memory", 0) for ds in datasets]
        offset = (i - len(tools)/2 + 0.5) * width
        bars = ax.bar(x + offset, memory, width, label=tool, color=colors.get(tool, "#999999"))
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h, f'{h:.1f}', ha='center', va='bottom', fontsize=9)

    ax.set_ylabel('Memory Usage (MB)', fontsize=12)
    ax.set_title('Memory Consumption Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'{ds.capitalize()}\n(7.3 MB)' if ds == 'svedala' else f'{ds.capitalize()}\n(86.5 MB)' for ds in datasets])
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "memory_comparison.svg", format='svg', bbox_inches='tight')
    print("   → memory_comparison.svg")

    # Query comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, tool in enumerate(tools):
        query_times = [np.mean(data[ds].get(tool, {}).get("queries", [0])) for ds in datasets]
        offset = (i - len(tools)/2 + 0.5) * width
        bars = ax.bar(x + offset, query_times, width, label=tool, color=colors.get(tool, "#999999"))
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h, f'{h:.2f}', ha='center', va='bottom', fontsize=9)

    ax.set_ylabel('Average Query Time (ms)', fontsize=12)
    ax.set_title('Query Performance Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'{ds.capitalize()}\n(7.3 MB)' if ds == 'svedala' else f'{ds.capitalize()}\n(86.5 MB)' for ds in datasets])
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "query_comparison.svg", format='svg', bbox_inches='tight')
    print("   → query_comparison.svg")


def main():
    results_dir = Path("results")
    graphs_dir = results_dir / "graphs"
    graphs_dir.mkdir(exist_ok=True)

    print("📊 Generating performance graphs...")

    data = load_benchmarks(results_dir)

    for dataset, tools_data in sorted(data.items()):
        print(f"   {dataset.capitalize()} dataset:")
        plot_dataset(dataset.capitalize(), tools_data, graphs_dir)

    if len(data) >= 2:
        print("   Cross-dataset comparisons:")
        plot_cross_dataset(data, graphs_dir)

    print(f"\n✅ Graph generation complete!\n   Location: {graphs_dir}/")


if __name__ == "__main__":
    try:
        import matplotlib
    except ImportError:
        print("❌ Error: matplotlib not installed")
        print("   Install with: uv sync --extra visualization")
        sys.exit(1)

    main()
