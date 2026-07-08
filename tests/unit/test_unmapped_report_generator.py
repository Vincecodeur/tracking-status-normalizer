from tracking_status_normalizer.catalog.unmapped_report_generator import (
    generate_unmapped_report,
)


def test_generate_report():
    unknown_statuses = {
        ("DHL", "Delivered to neighbour"): 53,
        ("UPS", "Customer requested hold"): 12,
    }

    report = generate_unmapped_report(
        unknown_statuses
    )

    assert report.total_unknown_statuses == 2

    assert (
        report.statuses[0].raw_status
        == "Delivered to neighbour"
    )

    assert report.statuses[0].occurrences == 53


def test_report_sorted_by_occurrence():
    unknown_statuses = {
        ("Carrier A", "Status A"): 5,
        ("Carrier B", "Status B"): 50,
        ("Carrier C", "Status C"): 15,
    }

    report = generate_unmapped_report(
        unknown_statuses
    )

    assert report.statuses[0].occurrences == 50
    assert report.statuses[1].occurrences == 15
    assert report.statuses[2].occurrences == 5