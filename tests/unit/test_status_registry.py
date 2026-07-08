from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.shipment_outcome import ShipmentOutcome
from tracking_status_normalizer.domain.status_registry import STATUS_REGISTRY


def test_delivered_outcome():
    status = STATUS_REGISTRY[CanonicalStatus.DELIVERED]

    assert status.outcome == ShipmentOutcome.SUCCESS


def test_lost_is_terminal():
    status = STATUS_REGISTRY[CanonicalStatus.LOST]

    assert status.terminal is True