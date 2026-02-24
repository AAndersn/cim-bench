"""RDFlib parser adapter for benchmarking.

RDFlib is a Python library for working with RDF (Resource Description Framework).
Uses Oxigraph store for high-performance in-memory SPARQL queries.
Repository: https://github.com/RDFLib/rdflib
Documentation: https://rdflib.readthedocs.io/
"""

import tempfile
import zipfile
from pathlib import Path
from rdflib import Graph
from parser_adapter import ParserAdapter
from datasets import DATASETS


class RDFlibAdapter(ParserAdapter):
    """Adapter for RDFlib library with Oxigraph store."""

    def __init__(self):
        self.libgraph = None
        self.cim_namespace = None  # Will be detected from loaded data

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "RDFlib"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#f1c40f"  # Yellow

    def load(self, dataset_key: str):
        """Load using RDFlib with Oxigraph store."""
        dataset = DATASETS[dataset_key]

        # Use Oxigraph store for better performance
        self.libgraph = Graph(store='Oxigraph')

        if "ZIP" in dataset:
            # Single ZIP file (RealGrid) - load EQ files only to avoid duplicates
            # due to rdf:ID creating file-specific URIs
            with tempfile.TemporaryDirectory() as tmpdir:
                with zipfile.ZipFile(dataset["ZIP"], 'r') as zf:
                    zf.extractall(tmpdir)
                    # Parse EQ (Equipment) files only for canonical counts
                    # Try multiple naming patterns: *_EQ_*.xml, *_EQ.xml, *EQ.xml
                    eq_files = list(Path(tmpdir).rglob("*_EQ_*.xml"))
                    eq_files.extend(Path(tmpdir).rglob("*_EQ.xml"))
                    eq_files.extend(Path(tmpdir).rglob("*EQ.xml"))

                    for xml_file in set(eq_files):  # Use set to avoid duplicates
                        self.libgraph.parse(xml_file)
        else:
            # Multiple files (Svedala) - load EQ file only
            # SSH/SV/TP files reference equipment but use file-specific URIs
            # with rdf:ID, causing duplicates
            if "EQ" in dataset:
                self.libgraph.parse(dataset["EQ"])
            else:
                # Fallback: load all files if no EQ file specified
                files = [v for k, v in dataset.items() if k != "_metadata"]
                for file_path in files:
                    self.libgraph.parse(file_path)

        # Detect CIM namespace from loaded data
        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF graph."""
        # Try common CIM namespaces
        namespaces = [
            "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
            "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
        ]

        # Query to find which namespace is used
        for ns in namespaces:
            test_query = f'''
            ASK {{
                ?s a <{ns}ACLineSegment> .
            }}
            '''
            if self.libgraph.query(test_query).askAnswer:
                self.cim_namespace = ns
                return

        # Default to CIM100 if nothing found
        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _count_instances(self, class_name: str) -> int:
        """Count instances of a CIM class using SPARQL."""
        if not self.cim_namespace:
            self._detect_namespace()

        query = f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{
            ?s a <{self.cim_namespace}{class_name}> .
        }}
        '''
        result = list(self.libgraph.query(query))
        return int(result[0][0])

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from RDF graph."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": len(loaded_obj.libgraph),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.libgraph is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.libgraph is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.libgraph is None:
            raise ValueError("No data loaded")
        conform = loaded_obj._count_instances("ConformLoad")
        nonconform = loaded_obj._count_instances("NonConformLoad")
        energy_consumer = loaded_obj._count_instances("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.libgraph is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("Substation")
