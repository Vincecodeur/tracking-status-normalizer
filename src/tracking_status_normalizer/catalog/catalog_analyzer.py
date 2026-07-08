"""
Catalog analyzer.
"""

from tracking_status_normalizer.normalization.mapping_loader import (
    MappingRegistry,
)

from tracking_status_normalizer.catalog.catalog_stats import (
    CatalogStats,
)


def analyze_catalog(
    carrier: str,
    mapping_registry: MappingRegistry,
) -> CatalogStats:
    """
    Analyze catalog statistics for a carrier.
    """

    carrier_key = carrier.strip().lower()

    carrier_mappings = [
        canonical
        for (carrier_name, _), canonical
        in mapping_registry.items()
        if carrier_name == carrier_key
    ]

    return CatalogStats(
        carrier=carrier,
        total_mappings=len(carrier_mappings),
        unique_canonical_statuses=len(
            set(carrier_mappings)
        ),
    )