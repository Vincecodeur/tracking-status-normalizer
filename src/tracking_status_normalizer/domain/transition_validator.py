"""
Validation engine for tracking status transitions.
"""

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.transition_registry import ALLOWED_TRANSITIONS


def is_transition_allowed(
    source: CanonicalStatus,
    target: CanonicalStatus,
) -> bool:
    """
    Returns True if a transition is allowed.

    Example:
        IN_TRANSIT -> OUT_FOR_DELIVERY => True

        DELIVERED -> IN_TRANSIT => False
    """

    allowed_targets = ALLOWED_TRANSITIONS.get(source, set())

    return target in allowed_targets