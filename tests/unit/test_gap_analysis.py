from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.governance.gaps.gap_analysis import (
    analyze_gaps,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


def test_no_gap_when_nothing_missing():
    results = [
        CoverageResult(
            capability=Capability.RETURNS,
            level=CoverageLevel.FULL,
            required_statuses=3,
            covered_statuses=3,
            missing_statuses=[],
        )
    ]

    gaps = analyze_gaps(results)

    assert gaps == []


def test_core_gap_is_critical():
    results = [
        CoverageResult(
            capability=Capability.DIRECT_DELIVERY,
            level=CoverageLevel.NONE,
            required_statuses=3,
            covered_statuses=0,
            missing_statuses=[
                CanonicalStatus.DELIVERED,
            ],
        )
    ]

    gaps = analyze_gaps(results)

    assert len(gaps) == 1
    assert gaps[0].severity == GapSeverity.CRITICAL


def test_extended_gap_is_medium():
    results = [
        CoverageResult(
            capability=Capability.RETURNS,
            level=CoverageLevel.NONE,
            required_statuses=3,
            covered_statuses=0,
            missing_statuses=[
                CanonicalStatus.RETURN_DELIVERED,
            ],
        )
    ]

    gaps = analyze_gaps(results)

    assert len(gaps) == 1
    assert gaps[0].severity == GapSeverity.MEDIUM


def test_extended_partial_gap_is_low():
    results = [
        CoverageResult(
            capability=Capability.RETURNS,
            level=CoverageLevel.PARTIAL,
            required_statuses=3,
            covered_statuses=2,
            missing_statuses=[
                CanonicalStatus.RETURN_DELIVERED,
            ],
        )
    ]

    gaps = analyze_gaps(results)

    assert len(gaps) == 1
    assert gaps[0].severity == GapSeverity.LOW