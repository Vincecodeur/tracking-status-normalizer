from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.gaps.gap_rules import (
    determine_gap_severity,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


def test_core_none_is_critical():
    severity = determine_gap_severity(
        Capability.DIRECT_DELIVERY,
        CoverageLevel.NONE,
    )

    assert severity == GapSeverity.CRITICAL


def test_core_partial_is_medium():
    severity = determine_gap_severity(
        Capability.DIRECT_DELIVERY,
        CoverageLevel.PARTIAL,
    )

    assert severity == GapSeverity.MEDIUM


def test_extended_none_is_medium():
    severity = determine_gap_severity(
        Capability.RETURNS,
        CoverageLevel.NONE,
    )

    assert severity == GapSeverity.MEDIUM


def test_extended_partial_is_low():
    severity = determine_gap_severity(
        Capability.RETURNS,
        CoverageLevel.PARTIAL,
    )

    assert severity == GapSeverity.LOW