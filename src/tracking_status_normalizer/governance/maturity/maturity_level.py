"""
Maturity level definitions.
"""

from enum import Enum


class MaturityLevel(str, Enum):
    """
    Catalog maturity levels.

    BASIC:
        Catalog is minimally usable.

    DEVELOPING:
        Core coverage is present but significant gaps remain.

    MATURE:
        Catalog is operationally strong with limited gaps.

    ADVANCED:
        Catalog provides comprehensive coverage with no significant gaps.
    """

    BASIC = "BASIC"

    DEVELOPING = "DEVELOPING"

    MATURE = "MATURE"

    ADVANCED = "ADVANCED"