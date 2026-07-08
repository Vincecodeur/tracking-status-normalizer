from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.normalization.normalizer import normalize


def test_normalize_known_status():
    registry = {
        ("dhl", "shipment delivered"): CanonicalStatus.DELIVERED,
    }

    result = normalize(
        "DHL",
        "Shipment delivered",
        registry,
    )

    assert result.carrier == "DHL"
    assert result.raw_status == "Shipment delivered"
    assert result.canonical_status == CanonicalStatus.DELIVERED
    assert result.mapped is True


def test_normalize_unknown_status():
    registry = {
        ("dhl", "shipment delivered"): CanonicalStatus.DELIVERED,
    }

    result = normalize(
        "DHL",
        "Unknown status",
        registry,
    )

    assert result.carrier == "DHL"
    assert result.raw_status == "Unknown status"
    assert result.canonical_status is None
    assert result.mapped is False


def test_normalize_with_accents_and_punctuation():
    registry = {
        ("colissimo", "votre colis est livre"): CanonicalStatus.DELIVERED,
    }

    result = normalize(
        "Colissimo",
        "Votre colis est livré.",
        registry,
    )

    assert result.canonical_status == CanonicalStatus.DELIVERED
    assert result.mapped is True