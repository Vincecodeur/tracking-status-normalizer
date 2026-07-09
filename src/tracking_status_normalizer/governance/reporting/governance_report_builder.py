"""
Governance report builder.
"""

from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.maturity.maturity_result import (
    MaturityResult,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)
from tracking_status_normalizer.governance.recommendations.recommendation import (
    Recommendation,
)
from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def build_governance_report(
    coverage_results: list[CoverageResult],
    readiness_result: ReadinessResult,
    gaps: list[Gap],
    recommendations: list[Recommendation],
    maturity_result: MaturityResult,
) -> GovernanceReport:
    """
    Build a consolidated governance report.
    """

    return GovernanceReport(
        coverage_results=coverage_results,
        readiness_result=readiness_result,
        gaps=gaps,
        recommendations=recommendations,
        maturity_result=maturity_result,
    )