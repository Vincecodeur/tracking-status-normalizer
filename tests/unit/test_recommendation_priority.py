from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)


def test_recommendation_priority_values():
    assert RecommendationPriority.HIGH.value == "HIGH"
    assert RecommendationPriority.MEDIUM.value == "MEDIUM"
    assert RecommendationPriority.LOW.value == "LOW"