"""
Tracking status normalizer.
"""

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.normalization.mapping_loader import (
    MappingRegistry,
)
from tracking_status_normalizer.normalization.text_normalizer import (
    normalize_text,
)


def normalize(
    carrier: str,
    raw_status: str,
    mapping_registry: MappingRegistry,
) -> CanonicalStatus | None:
    """
    Convert a raw carrier status into a canonical status.

    Args:
        carrier: Carrier name.
        raw_status: Raw status received from the carrier.
        mapping_registry: Loaded mapping registry.

    Returns:
        CanonicalStatus if a mapping exists.
        None otherwise.
    """

    key = (
        normalize_text(carrier),
        normalize_text(raw_status),
    )

    return mapping_registry.get(key)