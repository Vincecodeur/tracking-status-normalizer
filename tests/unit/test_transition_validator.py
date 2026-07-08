from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.domain.transition_validator import (
    is_transition_allowed,
)


def test_valid_transition():
    """
    A shipment moving toward delivery should be valid.
    """

    assert is_transition_allowed(
        CanonicalStatus.IN_TRANSIT,
        CanonicalStatus.OUT_FOR_DELIVERY,
    )


def test_invalid_transition():
    """
    A delivered shipment cannot go back into transit.
    """

    assert not is_transition_allowed(
        CanonicalStatus.DELIVERED,
        CanonicalStatus.IN_TRANSIT,
    )


def test_return_after_delivery():
    """
    Option B:
    Delivered shipments may enter a return flow.
    """

    assert is_transition_allowed(
        CanonicalStatus.DELIVERED,
        CanonicalStatus.RETURN_INITIATED,
    )