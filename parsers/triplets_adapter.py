"""Triplets parser adapter for benchmarking.

Triplets is a Python library for parsing CIM RDF/XML data to pandas DataFrames.
Repository: https://github.com/Baltic-RCC/triplets
Documentation: https://haigutus.github.io/triplets/
"""

import pandas
import triplets  # noqa: F401 - Extends pandas with read_RDF
from parser_adapter import ParserAdapter
from datasets import DATASETS, get_size_mb


class TripletsAdapter(ParserAdapter):
    """Adapter for triplets library."""

    def __init__(self):
        self.df = None

    def load(self, dataset_key: str):
        """Load using triplets library directly."""
        dataset = DATASETS[dataset_key]

        if "ZIP" in dataset:
            # Single ZIP file (RealGrid)
            self.df = pandas.read_RDF(str(dataset["ZIP"]))
        else:
            # Multiple files (Svedala)
            files = [v for k, v in dataset.items() if k != "_metadata"]
            self.df = pandas.read_RDF([str(f) for f in files])

        return self

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from triplets dataframe."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triplets_count": len(loaded_obj.df),
            "unique_objects": loaded_obj.df['ID'].nunique(),
            "instances": loaded_obj.df['INSTANCE_ID'].nunique(),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        return loaded_obj.df.query("KEY == 'Type' & VALUE == 'ACLineSegment'")["ID"].nunique()

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        return loaded_obj.df.query("KEY == 'Type' & VALUE == 'SynchronousMachine'")["ID"].nunique()

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        conform = loaded_obj.df.query("KEY == 'Type' & VALUE == 'ConformLoad'")["ID"].nunique()
        nonconform = loaded_obj.df.query("KEY == 'Type' & VALUE == 'NonConformLoad'")["ID"].nunique()
        energy_consumer = loaded_obj.df.query("KEY == 'Type' & VALUE == 'EnergyConsumer'")["ID"].nunique()
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        return loaded_obj.df.query("KEY == 'Type' & VALUE == 'Substation'")["ID"].nunique()
