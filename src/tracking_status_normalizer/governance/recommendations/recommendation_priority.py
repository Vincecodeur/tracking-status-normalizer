"""
Recommendation priority definitions.
"""

from enum import Enum


class RecommendationPriority(str, Enum):
    """
    Recommendation priority.

    HIGH:
        Immediate action recommended.

    MEDIUM:
        Improvement recommended.

    LOW:
        Optional enhancement.
    """

    HIGH = "HIGH"

    MEDIUM = "MEDIUM"

    LOW = "LOW"
