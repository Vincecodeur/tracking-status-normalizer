"""
Governance report model.
"""

from dataclasses import dataclass

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


@dataclass(frozen=True)
class GovernanceReport:
    """
    Consolidated governance report.

    Attributes:
        coverage_results:
            Operational coverage evaluation.

        readiness_result:
            Catalog readiness assessment.

        gaps:
            Identified catalog gaps.

        recommendations:
            Recommended improvements.

        maturity_result:
            Catalog maturity assessment.
    """

    coverage_results: list[CoverageResult]

    readiness_result: ReadinessResult

    gaps: list[Gap]

    recommendations: list[Recommendation]

    maturity_result: MaturityResult