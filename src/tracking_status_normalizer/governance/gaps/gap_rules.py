"""
Gap severity rules.
"""

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


CORE_CAPABILITIES = {
    Capability.DIRECT_DELIVERY,
    Capability.EXCEPTION_MANAGEMENT,
}


def determine_gap_severity(
    capability: Capability,
    coverage_level: CoverageLevel,
) -> GapSeverity:
    """
    Determine gap severity.

    Rules:

    CORE + NONE     -> CRITICAL
    CORE + PARTIAL  -> MEDIUM

    EXTENDED + NONE    -> MEDIUM
    EXTENDED + PARTIAL -> LOW
    """

    if capability in CORE_CAPABILITIES:

        if coverage_level == CoverageLevel.NONE:
            return GapSeverity.CRITICAL

        return GapSeverity.MEDIUM

    if coverage_level == CoverageLevel.NONE:
        return GapSeverity.MEDIUM

    return GapSeverity.LOW
