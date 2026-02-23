"""Benchmark for pypowsybl library - RealGrid dataset (86.5MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from pypowsybl_adapter import PypowsyblAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=PypowsyblAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="pypowsybl",
    dataset_name="realgrid"
)
