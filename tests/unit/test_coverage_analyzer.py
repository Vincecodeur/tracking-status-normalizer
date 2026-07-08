from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.normalization.coverage_analyzer import (
    analyze_coverage,
)


def test_full_coverage():
    registry = {
        ("dhl", "shipment delivered"): CanonicalStatus.DELIVERED,
        ("dhl", "shipment in transit"): CanonicalStatus.IN_TRANSIT,
    }

    result = analyze_coverage(
        carrier="DHL",
        statuses=[
            "Shipment delivered",
            "Shipment in transit",
        ],
        mapping_registry=registry,
    )

    assert result.total_statuses == 2
    assert result.mapped_statuses == 2
    assert result.unmapped_statuses == 0
    assert result.coverage_percentage == 100.0


def test_partial_coverage():
    registry = {
        ("dhl", "shipment delivered"): CanonicalStatus.DELIVERED,
    }

    result = analyze_coverage(
        carrier="DHL",
        statuses=[
            "Shipment delivered",
            "Unknown status",
        ],
        mapping_registry=registry,
    )

    assert result.total_statuses == 2
    assert result.mapped_statuses == 1
    assert result.unmapped_statuses == 1
    assert result.coverage_percentage == 50.0


def test_zero_statuses():
    registry = {}

    result = analyze_coverage(
        carrier="DHL",
        statuses=[],
        mapping_registry=registry,
    )

    assert result.total_statuses == 0
    assert result.coverage_percentage == 0.0
