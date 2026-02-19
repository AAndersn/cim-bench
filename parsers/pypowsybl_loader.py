"""
pypowsybl library wrapper for CIM-bench.

pypowsybl is a Python binding for PowSyBl (Power System Blocks),
an open-source framework for power system modeling and analysis.
Repository: https://github.com/powsybl/pypowsybl
Documentation: https://pypowsybl.readthedocs.io/
"""

import pypowsybl.network as pn
from pathlib import Path
import zipfile
import tempfile
import os


class PypowsyblLoader:
    """Wrapper for pypowsybl library."""

    def __init__(self):
        self.network = None

    def load_file(self, file_path):
        """Load a single CIM/CGMES file or ZIP."""
        self.network = pn.load(file_path)
        return self.network

    def load_cgmes_files(self, file_paths, include_common_data=True):
        """
        Load multiple CGMES files.

        For CGMES, pypowsybl requires a ZIP file or all files in the same directory.
        This method creates a temporary ZIP file with all provided files.

        Args:
            file_paths: List of paths to CGMES files (EQ, SSH, SV, TP, etc.)
            include_common_data: If True, includes CommonData and Boundary files
        """
        # Create temporary ZIP file
        tmp_zip = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)

        try:
            with zipfile.ZipFile(tmp_zip.name, "w") as zf:
                for file_path in file_paths:
                    p = Path(file_path)
                    zf.write(p, arcname=p.name)

            self.network = pn.load(tmp_zip.name)
            return self.network
        finally:
            os.unlink(tmp_zip.name)

    def get_buses(self):
        """Get all buses in the network."""
        if self.network is None:
            raise ValueError("No network loaded")
        return self.network.get_buses()

    def get_lines(self):
        """Get all lines in the network."""
        if self.network is None:
            raise ValueError("No network loaded")
        return self.network.get_lines()

    def get_generators(self):
        """Get all generators in the network."""
        if self.network is None:
            raise ValueError("No network loaded")
        return self.network.get_generators()

    def get_loads(self):
        """Get all loads in the network."""
        if self.network is None:
            raise ValueError("No network loaded")
        return self.network.get_loads()

    def get_substations(self):
        """Get all substations in the network."""
        if self.network is None:
            raise ValueError("No network loaded")
        return self.network.get_substations()

    def get_stats(self):
        """Get statistics about loaded network."""
        if self.network is None:
            return {}

        return {
            "bus_count": len(self.network.get_buses()),
            "line_count": len(self.network.get_lines()),
            "generator_count": len(self.network.get_generators()),
            "load_count": len(self.network.get_loads()),
            "substation_count": len(self.network.get_substations()),
        }
