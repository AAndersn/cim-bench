"""Dataset definitions for CIM-bench."""

from pathlib import Path

_DATA_ROOT = Path(__file__).parent.parent / "data" / "relicapgrid" / "Instance" / "Grid"

DATASETS = {
    "svedala_igm_cgmes_3": {
        "EQ": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z__Svedala_EQ_1.xml",
        "SSH": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_SSH_1.xml",
        "SV": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_SV_1.xml",
        "TP": _DATA_ROOT / "IGM_Svedala" / "20220615T2230Z_2D_Svedala_TP_1.xml",
        "COMMON": _DATA_ROOT / "CommonAndBoundaryData" / "CommonData_and_Boundary_merged.xml",
    },
}


def get_size_mb(files):
    """Get total size of files in MB."""
    return sum(f.stat().st_size for f in files if f.exists()) / 1024 / 1024
