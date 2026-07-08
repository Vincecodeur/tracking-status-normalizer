from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.processing.shipment_processor import (
    process_shipment,
)


def test_process_successful_delivery():
    registry = {
        ("dhl", "shipment in transit"):
            CanonicalStatus.IN_TRANSIT,

        ("dhl", "out for delivery"):
            CanonicalStatus.OUT_FOR_DELIVERY,

        ("dhl", "shipment delivered"):
            CanonicalStatus.DELIVERED,
    }

    result = process_shipment(
        carrier="DHL",
        statuses=[
            "Shipment in transit",
            "Out for delivery",
            "Shipment delivered",
        ],
        mapping_registry=registry,
    )

    assert result.validation.valid is True

    assert (
        result.lifecycle.current_status
        == CanonicalStatus.DELIVERED
    )

    assert result.mapped_statuses == 3

    assert result.unmapped_statuses == 0


def test_process_with_unknown_status():
    registry = {
        ("dhl", "shipment delivered"):
            CanonicalStatus.DELIVERED,
    }

    result = process_shipment(
        carrier="DHL",
        statuses=[
            "Unknown status",
            "Shipment delivered",
        ],
        mapping_registry=registry,
    )

    assert result.mapped_statuses == 1

    assert result.unmapped_statuses == 1