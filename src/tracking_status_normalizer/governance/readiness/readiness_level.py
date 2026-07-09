"""
Readiness level definitions.

This module defines the readiness levels used by the
Governance Layer.

Readiness indicates whether a carrier catalog is suitable
for operational usage with the Tracking Status Normalizer Engine.
"""

from enum import Enum


class ReadinessLevel(str, Enum):
    """
    Readiness assessment result.

    GO:
        All CORE capabilities are fully covered.

    GO_WITH_RISKS:
        All CORE capabilities are fully covered,
        but one or more EXTENDED capabilities are
        partially or not covered.

    NO_GO:
        One or more CORE capabilities are partially
        or not covered.
    """

    GO = "GO"

    GO_WITH_RISKS = "GO_WITH_RISKS"

    NO_GO = "NO_GO"