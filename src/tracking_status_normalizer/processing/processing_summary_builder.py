"""
Builds a ProcessingSummary from a ShipmentResult.
"""

from tracking_status_normalizer.processing.processing_summary import (
    ProcessingSummary,
)
from tracking_status_normalizer.processing.shipment_result import (
    ShipmentResult,
)


def build_processing_summary(
    carrier: str,
    result: ShipmentResult,
) -> ProcessingSummary:

    validation_status = (
        "VALID"
        if result.validation.valid
        else "INVALID"
    )

    return ProcessingSummary(
        carrier=carrier,

        current_status=(
            result.lifecycle.current_status.value
        ),

        outcome=(
            result.lifecycle.current_outcome.value
        ),

        validation_status=validation_status,

        mapped_statuses=result.mapped_statuses,

        unmapped_statuses=result.unmapped_statuses,
    )