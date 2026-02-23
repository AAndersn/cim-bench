"""Benchmark for VeraGrid library - Svedala IGM dataset (7.3MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from veragrid_adapter import VeragridAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=VeragridAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="veragrid",
    dataset_name="svedala"
)
