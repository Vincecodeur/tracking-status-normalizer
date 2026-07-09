"""
Tests for maturity scoring.
"""

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
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)
from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)
from tracking_status_normalizer.governance.maturity.maturity_score import (
    calculate_maturity,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)


def make_coverage_result(
    capability: Capability,
    level: CoverageLevel,
) -> CoverageResult:
    return CoverageResult(
        capability=capability,
        level=level,
        required_statuses=0,
        covered_statuses=0,
        missing_statuses=[],
    )


def make_gap(
    severity: GapSeverity,
) -> Gap:
    return Gap(
        capability=Capability.RETURNS,
        missing_status=CanonicalStatus.RETURN_DELIVERED,
        severity=severity,
    )


def test_calculate_maturity_advanced():
    coverage_results = [
        make_coverage_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_coverage_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
    ]

    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        [],
    )

    assert result.score == 100
    assert result.level == MaturityLevel.ADVANCED


def test_calculate_maturity_mature():
    coverage_results = [
        make_coverage_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.PARTIAL,
        ),
    ]

    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        [],
    )

    assert result.score == 95
    assert result.level == MaturityLevel.ADVANCED


def test_calculate_maturity_developing():
    coverage_results = [
        make_coverage_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.NONE,
        ),
    ]

    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO_WITH_RISKS,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        [
            make_gap(
                GapSeverity.MEDIUM,
            )
        ],
    )

    assert result.score == 72
    assert result.level == MaturityLevel.MATURE


def test_calculate_maturity_basic():
    coverage_results = [
        make_coverage_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.NONE,
        ),
        make_coverage_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.NONE,
        ),
    ]

    readiness_result = ReadinessResult(
        level=ReadinessLevel.NO_GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        [
            make_gap(
                GapSeverity.CRITICAL,
            ),
            make_gap(
                GapSeverity.CRITICAL,
            ),
            make_gap(
                GapSeverity.MEDIUM,
            ),
        ],
    )

    assert result.score == 17
    assert result.level == MaturityLevel.BASIC


def test_score_never_below_zero():
    coverage_results = [
        make_coverage_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.NONE,
        ),
        make_coverage_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.NONE,
        ),
    ]

    readiness_result = ReadinessResult(
        level=ReadinessLevel.NO_GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    gaps = [
        make_gap(GapSeverity.CRITICAL)
        for _ in range(20)
    ]

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        gaps,
    )

    assert result.score == 0


def test_score_never_above_hundred():
    coverage_results = []

    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        coverage_results,
        readiness_result,
        [],
    )

    assert result.score == 100


def test_no_go_reason_is_added():
    readiness_result = ReadinessResult(
        level=ReadinessLevel.NO_GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        [],
        readiness_result,
        [],
    )

    assert "NO_GO" in result.reasons[0]


def test_go_with_risks_reason_is_added():
    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO_WITH_RISKS,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    result = calculate_maturity(
        [],
        readiness_result,
        [],
    )

    assert "GO_WITH_RISKS" in result.reasons[0]