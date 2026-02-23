"""Benchmark for VeraGrid library - RealGrid dataset (86.5MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from veragrid_adapter import VeragridAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=VeragridAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="veragrid",
    dataset_name="realgrid"
)
