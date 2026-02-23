"""PyPowSyBl parser adapter for benchmarking.

pypowsybl is a Python binding for PowSyBl (Power System Blocks),
an open-source framework for power system modeling and analysis.
Repository: https://github.com/powsybl/pypowsybl
Documentation: https://pypowsybl.readthedocs.io/
"""

import tempfile
import zipfile
import os
from pathlib import Path

from parser_adapter import ParserAdapter
from datasets import DATASETS, get_size_mb
import pypowsybl.network as pn


class PypowsyblAdapter(ParserAdapter):
    """Adapter for pypowsybl library."""

    def __init__(self):
        self._temp_zip = None  # Track temp file for cleanup

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "PyPowSyBl"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#ff7f0e"  # Tab10 orange

    def load(self, dataset_key: str):
        """Load using pypowsybl."""
        dataset = DATASETS[dataset_key]

        if "ZIP" in dataset:
            # Already a ZIP (RealGrid)
            return pn.load(str(dataset["ZIP"]))
        else:
            # Multiple files - create temp ZIP (Svedala)
            files = [v for k, v in dataset.items() if k != "_metadata"]
            self._temp_zip = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
            with zipfile.ZipFile(self._temp_zip.name, "w") as zf:
                for f in files:
                    zf.write(f, arcname=f.name)
            return pn.load(self._temp_zip.name)

    def cleanup(self):
        """Cleanup temp ZIP if created."""
        if self._temp_zip:
            os.unlink(self._temp_zip.name)
            self._temp_zip = None

    def get_load_metrics(self, network, memory_mb):
        """Extract metrics from pypowsybl network."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "buses": len(network.get_buses()),
            "lines": len(network.get_lines()) + len(network.get_dangling_lines()),
            "ac_lines": len(network.get_lines()),
            "dangling_lines": len(network.get_dangling_lines()),
            "generators": len(network.get_generators()),
            "loads": len(network.get_loads()),
            "substations": len(network.get_substations()),
        }

    def get_lines_count(self, network):
        return len(network.get_lines())

    def get_generators_count(self, network):
        return len(network.get_generators())

    def get_loads_count(self, network):
        return len(network.get_loads())

    def get_substations_count(self, network):
        return len(network.get_substations())
