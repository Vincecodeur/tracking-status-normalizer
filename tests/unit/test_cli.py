import json

from tracking_status_normalizer.cli.main import main


def test_cli_process_valid_shipment(
    tmp_path,
    capsys,
):
    shipment_file = tmp_path / "shipment.json"

    mapping_file = tmp_path / "mapping.json"

    shipment_file.write_text(
        json.dumps(
            {
                "carrier": "DHL",
                "statuses": [
                    "Shipment in transit",
                    "Out for delivery",
                    "Shipment delivered",
                ],
            }
        ),
        encoding="utf-8",
    )

    mapping_file.write_text(
        json.dumps(
            {
                "mappings": [
                    {
                        "carrier": "DHL",
                        "raw_status": "Shipment in transit",
                        "canonical_status": "IN_TRANSIT",
                    },
                    {
                        "carrier": "DHL",
                        "raw_status": "Out for delivery",
                        "canonical_status": "OUT_FOR_DELIVERY",
                    },
                    {
                        "carrier": "DHL",
                        "raw_status": "Shipment delivered",
                        "canonical_status": "DELIVERED",
                    },
                ]
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(
        [
            "process",
            str(shipment_file),
            "--mapping",
            str(mapping_file),
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Tracking Status Normalizer" in captured.out
    assert "Carrier           : DHL" in captured.out
    assert "Validation        : VALID" in captured.out
    assert "Current Status    : DELIVERED" in captured.out
    assert "Outcome           : SUCCESS" in captured.out
    assert "Mapped Statuses   : 3" in captured.out
    assert "Unmapped Statuses : 0" in captured.out


def test_cli_process_missing_file(
    capsys,
):
    exit_code = main(
        [
            "process",
            "missing-file.json",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "ERROR" in captured.out
    assert "Shipment file not found" in captured.out