"""
Triplets library wrapper for CIM-bench.

Triplets is a Python library for parsing CIM RDF/XML data to pandas DataFrames.
Repository: https://github.com/Baltic-RCC/triplets
Documentation: https://haigutus.github.io/triplets/
"""

from triplets.rdf_parser import load_RDF_to_dataframe, type_tableview


class TripletsLoader:
    """Wrapper for triplets library."""

    def __init__(self):
        self.df = None

    def load_file(self, file_path):
        """Load a single CIM RDF/XML file."""
        self.df = load_RDF_to_dataframe(file_path)
        return self.df

    def load_files(self, file_paths):
        """Load multiple CIM RDF/XML files."""
        import pandas as pd

        dfs = []
        for path in file_paths:
            df = load_RDF_to_dataframe(path)
            dfs.append(df)

        self.df = pd.concat(dfs, ignore_index=True)
        return self.df

    def query_by_type(self, cim_type):
        """Query objects by CIM type."""
        if self.df is None:
            raise ValueError("No data loaded")
        return type_tableview(self.df, cim_type)

    def get_stats(self):
        """Get statistics about loaded data."""
        if self.df is None:
            return {}

        return {
            "triplet_count": len(self.df),
            "unique_objects": self.df["ID"].nunique(),
            "unique_instances": self.df["INSTANCE_ID"].nunique(),
        }
