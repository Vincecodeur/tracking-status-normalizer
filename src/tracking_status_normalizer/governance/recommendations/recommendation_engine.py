"""
Recommendation engine.
"""

from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)
from tracking_status_normalizer.governance.recommendations.recommendation import (
    Recommendation,
)
from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)



def generate_recommendations(
    gaps: list[Gap],
) -> list[Recommendation]:
    """
    Generate recommendations from identified gaps.
    """


    recommendations: list[Recommendation] = []

    for gap in gaps:

        priority = _get_priority(
            gap.severity
        )

        recommendations.append(
            Recommendation(
                priority=priority,
                capability=gap.capability,
                message=(
                    f"Add mapping for "
                    f"{gap.missing_status.value} "
                    f"to improve "
                    f"{gap.capability.value}."
                ),
            )
        )

    return recommendations


def _get_priority(
    severity: GapSeverity,
) -> RecommendationPriority:
    """
    Convert gap severity to recommendation priority.
    """

    if severity == GapSeverity.CRITICAL:
        return RecommendationPriority.HIGH

    if severity == GapSeverity.MEDIUM:
        return RecommendationPriority.MEDIUM

    return RecommendationPriority.LOW