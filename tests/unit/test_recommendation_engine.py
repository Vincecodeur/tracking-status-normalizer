from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.gaps.gap import (
    Gap,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)
from tracking_status_normalizer.governance.recommendations.recommendation_engine import (
    generate_recommendations,
)
from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)


def test_generate_high_priority_recommendation():
    gaps = [
        Gap(
            capability=Capability.DIRECT_DELIVERY,
            missing_status=CanonicalStatus.DELIVERED,
            severity=GapSeverity.CRITICAL,
        )
    ]

    recommendations = generate_recommendations(gaps)

    assert len(recommendations) == 1

    assert (
        recommendations[0].priority
        == RecommendationPriority.HIGH
    )

    assert (
        "DELIVERED"
        in recommendations[0].message
    )


def test_generate_medium_priority_recommendation():
    gaps = [
        Gap(
            capability=Capability.RETURNS,
            missing_status=CanonicalStatus.RETURN_DELIVERED,
            severity=GapSeverity.MEDIUM,
        )
    ]

    recommendations = generate_recommendations(gaps)

    assert len(recommendations) == 1

    assert (
        recommendations[0].priority
        == RecommendationPriority.MEDIUM
    )


def test_generate_low_priority_recommendation():
    gaps = [
        Gap(
            capability=Capability.RETURNS,
            missing_status=CanonicalStatus.RETURN_DELIVERED,
            severity=GapSeverity.LOW,
        )
    ]

    recommendations = generate_recommendations(gaps)

    assert len(recommendations) == 1

    assert (
        recommendations[0].priority
        == RecommendationPriority.LOW
    )


def test_generate_multiple_recommendations():
    gaps = [
        Gap(
            capability=Capability.DIRECT_DELIVERY,
            missing_status=CanonicalStatus.DELIVERED,
            severity=GapSeverity.CRITICAL,
        ),
        Gap(
            capability=Capability.RETURNS,
            missing_status=CanonicalStatus.RETURN_DELIVERED,
            severity=GapSeverity.MEDIUM,
        ),
    ]

    recommendations = generate_recommendations(gaps)

    assert len(recommendations) == 2