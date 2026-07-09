"""
Tests for governance report builder.
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
from tracking_status_normalizer.governance.reporting.governance_report_builder import (
    build_governance_report,
)


def test_build_governance_report():
    readiness_result = ReadinessResult(
        level=ReadinessLevel.GO,
        blocking_capabilities=[],
        risk_capabilities=[],
        reasons=[],
    )

    maturity_result = MaturityResult(
        score=100,
        level=MaturityLevel.ADVANCED,
        reasons=[],
    )

    report = build_governance_report(
        coverage_results=[],
        readiness_result=readiness_result,
        gaps=[],
        recommendations=[],
        maturity_result=maturity_result,
    )

    assert report.coverage_results == []

    assert report.readiness_result == readiness_result

    assert report.gaps == []

    assert report.recommendations == []

    assert report.maturity_result == maturity_result