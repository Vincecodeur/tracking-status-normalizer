"""
Governance CLI services.
"""

from tracking_status_normalizer.governance.coverage.operational_coverage import (
    evaluate_operational_coverage,
)
from tracking_status_normalizer.governance.gaps.gap_analysis import (
    analyze_gaps,
)
from tracking_status_normalizer.governance.maturity.maturity_score import (
    calculate_maturity,
)
from tracking_status_normalizer.governance.readiness.readiness_assessment import (
    assess_readiness,
)
from tracking_status_normalizer.governance.recommendations.recommendation_engine import (
    generate_recommendations,
)
from tracking_status_normalizer.governance.reporting.governance_report_builder import (
    build_governance_report,
)
from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)


def build_governance_report_from_statuses(
    statuses: set[CanonicalStatus],
):
    """
    Execute the complete governance pipeline.
    """

    coverage_results = evaluate_operational_coverage(
        statuses
    )

    readiness_result = assess_readiness(
        coverage_results
    )

    gaps = analyze_gaps(
        coverage_results
    )

    recommendations = generate_recommendations(
        gaps
    )

    maturity_result = calculate_maturity(
        coverage_results,
        readiness_result,
        gaps,
    )

    return build_governance_report(
        coverage_results=coverage_results,
        readiness_result=readiness_result,
        gaps=gaps,
        recommendations=recommendations,
        maturity_result=maturity_result,
    )