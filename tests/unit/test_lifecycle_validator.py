from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.validation.lifecycle_validator import (
    validate_lifecycle,
)


def test_valid_lifecycle():
    result = validate_lifecycle(
        [
            CanonicalStatus.INFO_RECEIVED,
            CanonicalStatus.PICKED_UP,
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
            CanonicalStatus.DELIVERED,
        ]
    )

    assert result.valid is True


def test_invalid_lifecycle():
    result = validate_lifecycle(
        [
            CanonicalStatus.DELIVERED,
            CanonicalStatus.IN_TRANSIT,
        ]
    )

    assert result.valid is False


def test_empty_lifecycle():
    result = validate_lifecycle([])

    assert result.valid is False


def test_single_status():
    result = validate_lifecycle(
        [CanonicalStatus.IN_TRANSIT]
    )

    assert result.valid is True