"""
Shipment lifecycle validation engine.
"""

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.transition_validator import (
    is_transition_allowed,
)
from tracking_status_normalizer.validation.validation_result import (
    ValidationResult,
)


def validate_lifecycle(
    statuses: list[CanonicalStatus],
) -> ValidationResult:
    """
    Validate a complete shipment lifecycle.

    Example:

        INFO_RECEIVED
            ↓
        PICKED_UP
            ↓
        IN_TRANSIT
            ↓
        DELIVERED

    Returns:
        ValidationResult
    """

    # Empty timeline is invalid.
    if not statuses:
        return ValidationResult(
            valid=False,
            reason="Lifecycle is empty.",
        )

    # A single status is valid by definition.
    if len(statuses) == 1:
        return ValidationResult(valid=True)

    # Compare each pair of statuses.
    for index in range(len(statuses) - 1):

        source = statuses[index]
        target = statuses[index + 1]

        if not is_transition_allowed(source, target):
            return ValidationResult(
                valid=False,
                reason=(
                    f"Invalid transition: "
                    f"{source.value} -> {target.value}"
                ),
            )

    return ValidationResult(valid=True)