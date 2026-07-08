"""
Shipment processor.

This module orchestrates:
- normalization
- lifecycle validation
- lifecycle analysis
"""

from tracking_status_normalizer.analysis.lifecycle_analyzer import (
    analyze_lifecycle,
)
from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.normalization.normalizer import (
    normalize,
)
from tracking_status_normalizer.processing.shipment_result import (
    ShipmentResult,
)
from tracking_status_normalizer.validation.lifecycle_validator import (
    validate_lifecycle,
)


def process_shipment(
    carrier: str,
    statuses: list[str],
    mapping_registry,
) -> ShipmentResult:
    """
    Process a complete shipment lifecycle.

    Args:
        carrier:
            Carrier name.

        statuses:
            Raw carrier statuses ordered chronologically.

        mapping_registry:
            Loaded mapping catalog.

    Returns:
        ShipmentResult
    """

    canonical_statuses: list[CanonicalStatus] = []

    mapped_statuses = 0

    unmapped_statuses = 0

    # Normalize every status.
    for raw_status in statuses:

        result = normalize(
            carrier=carrier,
            raw_status=raw_status,
            mapping_registry=mapping_registry,
        )

        if result.mapped:
            canonical_statuses.append(
                result.canonical_status
            )

            mapped_statuses += 1

        else:
            unmapped_statuses += 1

    validation = validate_lifecycle(
        canonical_statuses
    )

    lifecycle = analyze_lifecycle(
        canonical_statuses
    )

    return ShipmentResult(
        validation=validation,
        lifecycle=lifecycle,
        mapped_statuses=mapped_statuses,
        unmapped_statuses=unmapped_statuses,
    )