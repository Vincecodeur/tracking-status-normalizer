"""
Lifecycle summary model.

This module defines the object returned by the lifecycle analyzer.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.shipment_outcome import ShipmentOutcome
from tracking_status_normalizer.domain.status_category import StatusCategory


@dataclass(frozen=True)
class LifecycleSummary:
    """
    Represents the business summary of a shipment lifecycle.

    This object is useful for APIs, dashboards, reporting, and analytics.

    Attributes:
        current_status: Last known canonical status.
        current_category: Business category of the current status.
        current_outcome: Business outcome associated with the current status.
        is_terminal: True if no further transition is expected.
        has_exception: True if the lifecycle contains an exception-related status.
        has_return_flow: True if the lifecycle contains a return-related status.
    """

    current_status: CanonicalStatus
    current_category: StatusCategory
    current_outcome: ShipmentOutcome
    is_terminal: bool
    has_exception: bool
    has_return_flow: bool