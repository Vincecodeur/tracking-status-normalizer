from tracking_status_normalizer.normalization.text_normalizer import (
    normalize_text,
)


def test_normalize_text_lowercase():
    assert normalize_text("DELIVERED") == "delivered"


def test_normalize_text_removes_accents():
    assert normalize_text("livré") == "livre"


def test_normalize_text_removes_punctuation():
    assert normalize_text("Votre colis est livré.") == "votre colis est livre"


def test_normalize_text_collapses_spaces():
    assert normalize_text("  Package    delivered  ") == "package delivered"