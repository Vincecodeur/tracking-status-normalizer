from tracking_status_normalizer.analysis.lifecycle_analyzer import (
    analyze_lifecycle,
)
from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.shipment_outcome import ShipmentOutcome
from tracking_status_normalizer.domain.status_category import StatusCategory


def test_analyze_successful_home_delivery():
    summary = analyze_lifecycle(
        [
            CanonicalStatus.INFO_RECEIVED,
            CanonicalStatus.PICKED_UP,
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
            CanonicalStatus.DELIVERED,
        ]
    )

    assert summary.current_status == CanonicalStatus.DELIVERED
    assert summary.current_category == StatusCategory.DELIVERED
    assert summary.current_outcome == ShipmentOutcome.SUCCESS
    assert summary.is_terminal is False
    assert summary.has_exception is False
    assert summary.has_return_flow is False


def test_analyze_pickup_expired_return_flow():
    summary = analyze_lifecycle(
        [
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKUP_EXPIRED,
            CanonicalStatus.RETURN_INITIATED,
            CanonicalStatus.RETURN_IN_TRANSIT,
            CanonicalStatus.RETURN_DELIVERED,
        ]
    )

    assert summary.current_status == CanonicalStatus.RETURN_DELIVERED
    assert summary.current_category == StatusCategory.RETURN
    assert summary.current_outcome == ShipmentOutcome.RETURNED
    assert summary.is_terminal is True
    assert summary.has_exception is True
    assert summary.has_return_flow is True


def test_analyze_lost_shipment():
    summary = analyze_lifecycle(
        [
            CanonicalStatus.PICKED_UP,
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.LOST,
        ]
    )

    assert summary.current_status == CanonicalStatus.LOST
    assert summary.current_category == StatusCategory.EXCEPTION
    assert summary.current_outcome == ShipmentOutcome.FAILED
    assert summary.is_terminal is True
    assert summary.has_exception is True
    assert summary.has_return_flow is False


def test_empty_lifecycle_raises_error():
    try:
        analyze_lifecycle([])
    except ValueError as error:
        assert str(error) == "Cannot analyze an empty lifecycle."
    else:
        assert False, "Expected ValueError for empty lifecycle."