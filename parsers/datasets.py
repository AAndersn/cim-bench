"""Dataset definitions for CIM-bench."""

from pathlib import Path

_DATA_ROOT = Path(__file__).parent.parent / "data" / "relicapgrid" / "Instance" / "Grid"

DATASETS = {
    "svedala_igm_cgmes_3": {
        # Files
        "EQ": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z__Svedala_EQ_1.xml",
        "SSH": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_SSH_1.xml",
        "SV": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_SV_1.xml",
        "TP": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_TP_1.xml",
        "COMMON": _DATA_ROOT / "CommonAndBoundaryData" / "CommonData_and_Boundary_merged.xml",
        # Metadata
        "_metadata": {
            "cgmes_version": "3.0",
            "size_mb": 7.3,
            "description": "Svedala IGM - Small Swedish test network",
            "element_counts": {
                "lines": 97,
                "generators": 39,
                "loads": 73,
                "substations": 56,
            },
        },
    },
    "realgrid_cgmes_2_4": {
        # Files
        "ZIP": Path(__file__).parent.parent / "data/triplets/test_data/TestConfigurations_packageCASv2.0/RealGrid/CGMES_v2.4.15_RealGridTestConfiguration_v2.zip",
        # Metadata
        "_metadata": {
            "cgmes_version": "2.4.15",
            "size_mb": 86.5,  # uncompressed
            "size_mb_compressed": 3.7,
            "description": "RealGrid - Large pan-European test configuration",
            "element_counts": {
                "estimated": 10000,  # will measure during benchmarks
            },
        },
    },
}


def get_size_mb(files):
    """Get total size of files in MB."""
    return sum(f.stat().st_size for f in files if f.exists()) / 1024 / 1024
