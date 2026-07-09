from tracking_status_normalizer.governance.exporters.json_exporter import (
    export_to_json,
)
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


def test_export_to_json():
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

    result = export_to_json(
        report
    )

    assert "score" in result
    assert "ADVANCED" in result