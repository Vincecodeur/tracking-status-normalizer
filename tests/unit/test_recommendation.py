from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.recommendations.recommendation import (
    Recommendation,
)
from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)


def test_create_recommendation():
    recommendation = Recommendation(
        priority=RecommendationPriority.HIGH,
        capability=Capability.DIRECT_DELIVERY,
        message="Add DELIVERED mapping.",
    )

    assert recommendation.priority == RecommendationPriority.HIGH
    assert recommendation.capability == Capability.DIRECT_DELIVERY
    assert recommendation.message == "Add DELIVERED mapping."