import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from rdflib_adapter import RDFlibAdapter
from benchmark_template import create_benchmarks

create_benchmarks(
    adapter=RDFlibAdapter(),
    dataset_key="realgrid_cgmes_2_4",
    parser_name="rdflib",
    dataset_name="realgrid"
)
