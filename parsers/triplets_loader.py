"""
Triplets library wrapper for CIM-bench.

Triplets is a Python library for parsing CIM RDF/XML data to pandas DataFrames.
Repository: https://github.com/Baltic-RCC/triplets
Documentation: https://haigutus.github.io/triplets/
"""

import pandas
import triplets


class TripletsLoader:
    """Wrapper for triplets library."""

    def __init__(self):
        self.df = None

    def load_file(self, file_path):
        """Load a single CIM RDF/XML file."""
        self.df = pandas.read_RDF([file_path])
        return self.df

    def load_files(self, file_paths):
        """Load multiple CIM RDF/XML files."""

        self.df = pandas.read_RDF(file_paths)

        return self.df

    def query_by_type(self, cim_type):
        """Query objects by CIM type."""
        if self.df is None:
            raise ValueError("No data loaded")
        return self.df.type_tableview(cim_type)

    def get_lines(self):
        """Get all lines (ACLineSegments) in the network."""
        if self.df is None:
            raise ValueError("No data loaded")
        return self.df.query("KEY == 'Type' & VALUE == 'ACLineSegment'")["ID"].nunique()

    def get_generators(self):
        """Get all generators (SynchronousMachines) in the network."""
        if self.df is None:
            raise ValueError("No data loaded")
        return self.df.query("KEY == 'Type' & VALUE == 'SynchronousMachine'")["ID"].nunique()

    def get_loads(self):
        """Get all loads (ConformLoad + NonConformLoad) in the network."""
        if self.df is None:
            raise ValueError("No data loaded")
        conform = self.df.query("KEY == 'Type' & VALUE == 'ConformLoad'")["ID"].nunique()
        nonconform = self.df.query("KEY == 'Type' & VALUE == 'NonConformLoad'")["ID"].nunique()
        return conform + nonconform

    def get_substations(self):
        """Get all substations in the network."""
        if self.df is None:
            raise ValueError("No data loaded")
        return self.df.query("KEY == 'Type' & VALUE == 'Substation'")["ID"].nunique()

    def get_stats(self):
        """Get statistics about loaded data."""
        if self.df is None:
            return {}

        return {
            "triplet_count": len(self.df),
            "loaded_objects": self.df.types_dict(),
            "unique_objects": self.df["ID"].nunique(),
            "unique_instances": self.df["INSTANCE_ID"].nunique(),
            "line_count": self.get_lines(),
            "generator_count": self.get_generators(),
            "load_count": self.get_loads(),
            "substation_count": self.get_substations(),
        }
