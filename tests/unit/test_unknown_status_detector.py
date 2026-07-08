from tracking_status_normalizer.normalization.unknown_status_detector import (
    UnknownStatusDetector,
)


def test_register_unknown_status():
    detector = UnknownStatusDetector()

    detector.register(
        "DHL",
        "New unknown status",
    )

    statuses = detector.get_unknown_statuses()

    assert statuses[("DHL", "New unknown status")] == 1


def test_register_same_unknown_status_multiple_times():
    detector = UnknownStatusDetector()

    detector.register("DHL", "New unknown status")
    detector.register("DHL", "New unknown status")
    detector.register("DHL", "New unknown status")

    statuses = detector.get_unknown_statuses()

    assert statuses[("DHL", "New unknown status")] == 3


def test_register_different_unknown_statuses():
    detector = UnknownStatusDetector()

    detector.register("DHL", "Unknown DHL status")
    detector.register("UPS", "Unknown UPS status")

    statuses = detector.get_unknown_statuses()

    assert statuses[("DHL", "Unknown DHL status")] == 1
    assert statuses[("UPS", "Unknown UPS status")] == 1