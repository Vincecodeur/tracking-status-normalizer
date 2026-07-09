"""
Tests for governance report model.
"""

from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)
from tracking_status_normalizer.governance.maturity.maturity_result import (
    MaturityResult,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)
from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def test_create_governance_report():
    report = GovernanceReport(
        coverage_results=[],
        readiness_result=ReadinessResult(
            level=ReadinessLevel.GO,
            blocking_capabilities=[],
            risk_capabilities=[],
            reasons=[],
        ),
        gaps=[],
        recommendations=[],
        maturity_result=MaturityResult(
            score=100,
            level=MaturityLevel.ADVANCED,
            reasons=[],
        ),
    )

    assert report.coverage_results == []

    assert (
        report.readiness_result.level
        == ReadinessLevel.GO
    )

    assert report.gaps == []

    assert report.recommendations == []

    assert (
        report.maturity_result.level
        == MaturityLevel.ADVANCED
    )