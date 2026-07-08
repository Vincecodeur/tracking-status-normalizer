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

    assert result == CanonicalStatus.DELIVERED


def test_normalize_unknown_status():
    registry = {
        ("dhl", "shipment delivered"): CanonicalStatus.DELIVERED,
    }

    result = normalize(
        "DHL",
        "Unknown status",
        registry,
    )

    assert result is None


def test_normalize_with_accents_and_punctuation():
    registry = {
        ("colissimo", "votre colis est livre"): CanonicalStatus.DELIVERED,
    }

    result = normalize(
        "Colissimo",
        "Votre colis est livré.",
        registry,
    )

    assert result == CanonicalStatus.DELIVERED