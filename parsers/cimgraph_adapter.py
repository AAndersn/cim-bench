"""CIM-Graph parser adapter for benchmarking.

CIM-Graph (CIMantic Graphs) is a Python library for creating in-memory
knowledge graphs for CIM power system models with typed CIM objects.
Repository: https://github.com/PNNL-CIM-Tools/CIM-Graph
Documentation: https://github.com/PNNL-CIM-Tools/CIM-Documentation
"""

import importlib
import tempfile
import zipfile
from pathlib import Path
from rdflib import Graph
from cimgraph.databases.rdflib import RDFlibConnection
from cimgraph.databases import ConnectionParameters
from parser_adapter import ParserAdapter
from datasets import DATASETS


class CIMGraphAdapter(ParserAdapter):
    """Adapter for CIM-Graph library using RDFlibConnection."""

    def __init__(self):
        self.connection = None
        self.cim = None
        self.cim_profile = None

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "CIM-Graph"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#9467bd"  # Purple

    def load(self, dataset_key: str):
        """Load using CIM-Graph's RDFlibConnection."""
        dataset = DATASETS[dataset_key]

        # Detect CIM profile and parameters for this dataset
        self.cim_profile = self._get_cim_profile(dataset_key)
        namespace = self._get_namespace(dataset_key)
        iec_version = self._get_iec_version(dataset_key)

        # Pre-load all EQ files into a single RDFlib graph
        temp_graph = Graph(store='Oxigraph')

        if "ZIP" in dataset:
            # Single ZIP file (RealGrid) - extract and load EQ files
            with tempfile.TemporaryDirectory() as tmpdir:
                with zipfile.ZipFile(dataset["ZIP"], 'r') as zf:
                    zf.extractall(tmpdir)
                    # Parse EQ (Equipment) files only for canonical counts
                    eq_files = list(Path(tmpdir).rglob("*_EQ_*.xml"))
                    eq_files.extend(Path(tmpdir).rglob("*_EQ.xml"))
                    eq_files.extend(Path(tmpdir).rglob("*EQ.xml"))

                    for xml_file in set(eq_files):  # Use set to avoid duplicates
                        temp_graph.parse(xml_file)
        else:
            # Multiple files (Svedala) - load EQ file only
            if "EQ" in dataset:
                temp_graph.parse(dataset["EQ"])
            else:
                # Fallback: load all files if no EQ file specified
                files = [v for k, v in dataset.items() if k != "_metadata"]
                for file_path in files:
                    temp_graph.parse(file_path)

        # Create RDFlibConnection with parameters
        params = ConnectionParameters(
            cim_profile=self.cim_profile,
            namespace=namespace,
            iec61970_301=iec_version
        )

        self.connection = RDFlibConnection(params, use_oxigraph=True)
        # Inject the pre-loaded graph into the connection
        self.connection.libgraph = temp_graph

        # Load CIM profile module for typed access
        self.cim = importlib.import_module(f'cimgraph.data_profile.{self.cim_profile}')

        return self

    def _get_cim_profile(self, dataset_key: str) -> str:
        """Map dataset to CIM profile."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        if cgmes_version == "3.0":
            return "rc4_2021"  # CGMES 3.0 → rc4_2021 profile
        elif cgmes_version.startswith("2.4"):
            return "cim17v40"  # CGMES 2.4 → cim17v40 profile
        else:
            return "rc4_2021"  # Default

    def _get_namespace(self, dataset_key: str) -> str:
        """Get CIM namespace for dataset."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        if cgmes_version == "3.0":
            return "http://iec.ch/TC57/CIM100#"
        elif cgmes_version.startswith("2.4"):
            return "http://iec.ch/TC57/2013/CIM-schema-cim16#"
        else:
            return "http://iec.ch/TC57/CIM100#"

    def _get_iec_version(self, dataset_key: str) -> int:
        """Get IEC 61970-301 version."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        return 8 if cgmes_version == "3.0" else 6

    def _count_instances(self, class_name: str) -> int:
        """Count instances using CIM-Graph's RDFlibConnection."""
        namespace = self.connection.namespace
        query = f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{
            ?s a <{namespace}{class_name}> .
        }}
        '''
        result = self.connection.execute(query)
        return int(list(result)[0][0])

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from CIM-Graph connection."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": len(loaded_obj.connection.libgraph),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.connection is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.connection is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.connection is None:
            raise ValueError("No data loaded")
        conform = loaded_obj._count_instances("ConformLoad")
        nonconform = loaded_obj._count_instances("NonConformLoad")
        energy_consumer = loaded_obj._count_instances("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.connection is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("Substation")
