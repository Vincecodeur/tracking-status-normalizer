import json

from tracking_status_normalizer.io.shipment_loader import (
    load_shipment_file,
)


def test_load_valid_shipment_file(
    tmp_path,
):
    shipment_file = tmp_path / "shipment.json"

    shipment_file.write_text(
        json.dumps(
            {
                "carrier": "DHL",
                "statuses": [
                    "Shipment in transit",
                    "Shipment delivered",
                ],
            }
        ),
        encoding="utf-8",
    )

    shipment = load_shipment_file(
        shipment_file
    )

    assert shipment.carrier == "DHL"

    assert shipment.statuses == [
        "Shipment in transit",
        "Shipment delivered",
    ]


def test_missing_carrier(
    tmp_path,
):
    shipment_file = tmp_path / "shipment.json"

    shipment_file.write_text(
        json.dumps(
            {
                "statuses": [],
            }
        ),
        encoding="utf-8",
    )

    try:
        load_shipment_file(
            shipment_file
        )
    except ValueError as error:
        assert "carrier" in str(error)
    else:
        assert False


def test_missing_statuses(
    tmp_path,
):
    shipment_file = tmp_path / "shipment.json"

    shipment_file.write_text(
        json.dumps(
            {
                "carrier": "DHL",
            }
        ),
        encoding="utf-8",
    )

    try:
        load_shipment_file(
            shipment_file
        )
    except ValueError as error:
        assert "statuses" in str(error)
    else:
        assert False
