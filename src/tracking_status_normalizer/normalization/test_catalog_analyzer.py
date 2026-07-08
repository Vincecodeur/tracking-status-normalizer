from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)

from tracking_status_normalizer.catalog.catalog_analyzer import (
    analyze_catalog,
)


def test_catalog_statistics():
    registry = {
        ("dhl", "shipment delivered"):
            CanonicalStatus.DELIVERED,

        ("dhl", "package delivered"):
            CanonicalStatus.DELIVERED,

        ("dhl", "shipment in transit"):
            CanonicalStatus.IN_TRANSIT,
    }

    stats = analyze_catalog(
        "DHL",
        registry,
    )

    assert stats.carrier == "DHL"

    assert stats.total_mappings == 3

    assert stats.unique_canonical_statuses == 2