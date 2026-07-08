"""
Validation result object.

This object contains the outcome of a tracking lifecycle validation.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationResult:
    """
    Represents the result of a validation.

    Attributes:
        valid: True if validation succeeded.
        reason: Explanation when validation fails.
    """

    valid: bool
    reason: str | None = None