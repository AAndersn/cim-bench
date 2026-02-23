"""Benchmark for triplets library - RealGrid dataset (86.5MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from triplets_adapter import TripletsAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=TripletsAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="triplets",
    dataset_name="realgrid"
)
