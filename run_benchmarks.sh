#!/usr/bin/env bash
#
# Run all CIM-bench benchmarks and generate reports
#
# Usage:
#   ./run_benchmarks.sh [--quick]
#
# Options:
#   --quick    Run minimal rounds for faster iteration
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ============================================================================
# BENCHMARK CONFIGURATION
# Add new benchmarks here: "test_file:output_name:display_name"
# ============================================================================
BENCHMARKS=(
    "benchmarks/test_triplets_benchmark.py:triplets:Triplets"
    "benchmarks/test_pypowsybl_benchmark.py:pypowsybl:PyPowSyBl"
)

RESULTS_DIR="results"
BENCHMARK_OPTS=""

# Parse arguments
if [[ "$1" == "--quick" ]]; then
    BENCHMARK_OPTS="--benchmark-min-rounds=3"
    echo "Running in quick mode (minimal rounds)"
fi

# Create results directory
mkdir -p "$RESULTS_DIR"

echo "=================================="
echo "CIM-bench Benchmark Suite"
echo "=================================="
echo ""

# Run benchmarks
BENCHMARK_JSONS=()
for benchmark_spec in "${BENCHMARKS[@]}"; do
    IFS=':' read -r test_file output_name display_name <<< "$benchmark_spec"

    echo "📊 Running $display_name benchmarks..."
    pytest "$test_file" \
        --benchmark-only \
        --benchmark-json="$RESULTS_DIR/${output_name}_benchmark.json" \
        $BENCHMARK_OPTS
    echo "✅ $display_name benchmarks complete"
    echo ""

    BENCHMARK_JSONS+=("$RESULTS_DIR/${output_name}_benchmark.json")
done

# Generate markdown reports
echo "📝 Generating markdown reports..."
for benchmark_spec in "${BENCHMARKS[@]}"; do
    IFS=':' read -r test_file output_name display_name <<< "$benchmark_spec"

    python tools/generate_report.py \
        "$RESULTS_DIR/${output_name}_benchmark.json" \
        "$RESULTS_DIR/${output_name}_report.md"
    echo "   → ${output_name}_report.md"
done
echo ""

# Generate comparison summary if we have multiple benchmarks
if [ ${#BENCHMARK_JSONS[@]} -gt 1 ]; then
    echo "📊 Generating comparison summary..."
    python tools/generate_comparison.py "${BENCHMARK_JSONS[@]}" "$RESULTS_DIR/comparison_summary.md"
    echo "   → comparison_summary.md"
    echo ""
fi

echo "=================================="
echo "✅ All benchmarks complete!"
echo "=================================="
echo ""
echo "Results available in: $RESULTS_DIR/"
echo ""
echo "Reports:"
for benchmark_spec in "${BENCHMARKS[@]}"; do
    IFS=':' read -r test_file output_name display_name <<< "$benchmark_spec"
    echo "  - ${output_name}_report.md"
done
if [ ${#BENCHMARK_JSONS[@]} -gt 1 ]; then
    echo "  - comparison_summary.md"
fi
echo ""
