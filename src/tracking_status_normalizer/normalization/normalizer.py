"""
Tracking status normalizer.

This module converts carrier-specific statuses into canonical statuses.
"""

from tracking_status_normalizer.normalization.mapping_loader import (
    MappingRegistry,
)
from tracking_status_normalizer.normalization.normalization_result import (
    NormalizationResult,
)
from tracking_status_normalizer.normalization.text_normalizer import (
    normalize_text,
)


def normalize(
    carrier: str,
    raw_status: str,
    mapping_registry: MappingRegistry,
) -> NormalizationResult:
    """
    Convert a raw carrier status into a canonical status.

    Args:
        carrier:
            Carrier name (e.g. DHL, UPS, Colissimo).

        raw_status:
            Raw carrier status.

        mapping_registry:
            Registry loaded from the mapping catalog.

    Returns:
        NormalizationResult

    Example:

        normalize(
            "DHL",
            "Shipment delivered",
            registry,
        )

    Returns:

        NormalizationResult(
            carrier="DHL",
            raw_status="Shipment delivered",
            canonical_status=CanonicalStatus.DELIVERED,
            mapped=True,
        )
    """

    # Normalize the lookup key to avoid issues caused by:
    # - uppercase vs lowercase
    # - accents
    # - punctuation
    # - multiple spaces
    key = (
        normalize_text(carrier),
        normalize_text(raw_status),
    )

    # Attempt to find a canonical mapping.
    canonical_status = mapping_registry.get(key)

    # Return a structured result object instead of only
    # returning the canonical status.
    return NormalizationResult(
        carrier=carrier,
        raw_status=raw_status,
        canonical_status=canonical_status,
        mapped=canonical_status is not None,
    )