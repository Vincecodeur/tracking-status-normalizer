"""
Recommendation model.
"""

from dataclasses import dataclass

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.recommendations.recommendation_priority import (
    RecommendationPriority,
)


@dataclass(frozen=True)
class Recommendation:
    """
    Recommendation generated from a gap.

    Attributes:
        priority:
            Recommendation priority.

        capability:
            Capability impacted.

        message:
            Human-readable recommendation.
    """

    priority: RecommendationPriority

    capability: Capability

    message: str