"""
Shipment processing result.

This module defines the final business result returned by the
shipment processing engine.
"""

from dataclasses import dataclass

from tracking_status_normalizer.analysis.lifecycle_summary import (
    LifecycleSummary,
)
from tracking_status_normalizer.validation.validation_result import (
    ValidationResult,
)


@dataclass(frozen=True)
class ShipmentResult:
    """
    End-to-end shipment processing result.

    Attributes:
        validation:
            Lifecycle validation result.

        lifecycle:
            Lifecycle business summary.

        mapped_statuses:
            Number of successfully normalized statuses.

        unmapped_statuses:
            Number of unknown statuses.
    """

    validation: ValidationResult

    lifecycle: LifecycleSummary

    mapped_statuses: int

    unmapped_statuses: int
