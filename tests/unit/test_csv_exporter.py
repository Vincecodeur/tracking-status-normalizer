"""
Tests for CSV governance exporters.
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
from tracking_status_normalizer.governance.exporters.csv_exporter import (
    export_coverage_to_csv,
    export_gaps_to_csv,
    export_recommendations_to_csv,
    export_summary_to_csv,
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
from tracking_status_normalizer.governance.maturity.maturity_result import (
    MaturityResult,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)
from tracking_status_normalizer.governance.recommendations.recommendation import (
    Recommendation,
)
from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)
from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def build_report() -> GovernanceReport:
    return GovernanceReport(
        coverage_results=[
            CoverageResult(
                capability=Capability.DIRECT_DELIVERY,
                level=CoverageLevel.PARTIAL,
                required_statuses=3,
                covered_statuses=2,
                missing_statuses=[
                    CanonicalStatus.DELIVERED,
                ],
            )
        ],
        readiness_result=ReadinessResult(
            level=ReadinessLevel.GO_WITH_RISKS,
            blocking_capabilities=[],
            risk_capabilities=[
                Capability.RETURNS,
            ],
            reasons=[
                "RETURNS is NONE.",
            ],
        ),
        gaps=[
            Gap(
                capability=Capability.DIRECT_DELIVERY,
                missing_status=CanonicalStatus.DELIVERED,
                severity=GapSeverity.MEDIUM,
            )
        ],
        recommendations=[
            Recommendation(
                priority=RecommendationPriority.MEDIUM,
                capability=Capability.DIRECT_DELIVERY,
                message="Add mapping for DELIVERED.",
            )
        ],
        maturity_result=MaturityResult(
            score=85,
            level=MaturityLevel.MATURE,
            reasons=[
                "Catalog readiness is GO_WITH_RISKS.",
            ],
        ),
    )


def test_export_summary_to_csv():
    report = build_report()

    csv_content = export_summary_to_csv(
        report
    )

    assert "field,value" in csv_content

    assert "readiness_level,GO_WITH_RISKS" in csv_content

    assert "maturity_score,85" in csv_content

    assert "maturity_level,MATURE" in csv_content


def test_export_coverage_to_csv():
    report = build_report()

    csv_content = export_coverage_to_csv(
        report
    )

    assert (
        "capability,coverage_level,required_statuses,"
        "covered_statuses,missing_statuses"
        in csv_content
    )

    assert "DIRECT_DELIVERY,PARTIAL,3,2,DELIVERED" in csv_content


def test_export_gaps_to_csv():
    report = build_report()

    csv_content = export_gaps_to_csv(
        report
    )

    assert "capability,missing_status,severity" in csv_content

    assert "DIRECT_DELIVERY,DELIVERED,MEDIUM" in csv_content


def test_export_recommendations_to_csv():
    report = build_report()

    csv_content = export_recommendations_to_csv(
        report
    )

    assert "priority,capability,message" in csv_content

    assert (
        "MEDIUM,DIRECT_DELIVERY,Add mapping for DELIVERED."
        in csv_content
    )