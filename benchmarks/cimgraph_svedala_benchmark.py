import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimgraph_adapter import CIMGraphAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=CIMGraphAdapter(),
    dataset_key="svedala_igm_cgmes_3",
    parser_name="cimgraph",
    dataset_name="svedala"
)
