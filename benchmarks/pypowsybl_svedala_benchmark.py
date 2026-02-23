"""Benchmark for pypowsybl library - Svedala IGM dataset (7.3MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from pypowsybl_adapter import PypowsyblAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=PypowsyblAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="pypowsybl",
    dataset_name="svedala"
)
