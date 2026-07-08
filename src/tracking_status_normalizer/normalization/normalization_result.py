"""
Normalization result.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)


@dataclass(frozen=True)
class NormalizationResult:
    """
    Result of a normalization operation.
    """

    carrier: str
    raw_status: str

    # None if no mapping exists.
    canonical_status: CanonicalStatus | None

    # True if a mapping has been found.
    mapped: bool