"""
Lifecycle analyzer.

This module converts a list of canonical statuses into a business summary.
"""

from tracking_status_normalizer.analysis.lifecycle_summary import (
    LifecycleSummary,
)
from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.status_category import StatusCategory
from tracking_status_normalizer.domain.status_registry import STATUS_REGISTRY


RETURN_STATUSES = {
    CanonicalStatus.RETURN_INITIATED,
    CanonicalStatus.RETURN_IN_TRANSIT,
    CanonicalStatus.RETURN_DELIVERED,
}


EXCEPTION_STATUSES = {
    CanonicalStatus.EXCEPTION,
    CanonicalStatus.LOST,
    CanonicalStatus.DAMAGED,
    CanonicalStatus.HELD,
    CanonicalStatus.DELIVERY_ATTEMPT_FAILED,
    CanonicalStatus.ADDRESS_ISSUE,
    CanonicalStatus.RECIPIENT_UNAVAILABLE,
    CanonicalStatus.PICKUP_EXPIRED,
}


def analyze_lifecycle(
    statuses: list[CanonicalStatus],
) -> LifecycleSummary:
    """
    Analyze a shipment lifecycle and return its business summary.

    Args:
        statuses: Ordered list of canonical statuses.

    Returns:
        LifecycleSummary

    Raises:
        ValueError: If the lifecycle is empty.
    """

    if not statuses:
        raise ValueError("Cannot analyze an empty lifecycle.")

    # The last status represents the current known shipment status.
    current_status = statuses[-1]

    # The registry contains the metadata attached to the current status:
    # category, outcome, and terminal flag.
    current_definition = STATUS_REGISTRY[current_status]

    has_exception = any(status in EXCEPTION_STATUSES for status in statuses)

    has_return_flow = any(status in RETURN_STATUSES for status in statuses)

    return LifecycleSummary(
        current_status=current_status,
        current_category=current_definition.category,
        current_outcome=current_definition.outcome,
        is_terminal=current_definition.terminal,
        has_exception=has_exception,
        has_return_flow=has_return_flow,
    )