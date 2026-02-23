"""Benchmark for triplets library - Svedala IGM dataset (7.3MB)."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from triplets_adapter import TripletsAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=TripletsAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="triplets",
    dataset_name="svedala"
)
