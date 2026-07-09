import json

from fastapi.testclient import TestClient

from tracking_status_normalizer.api.app import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
    }


def test_process_valid_shipment(tmp_path):
    mapping_file = tmp_path / "mapping.json"

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

    response = client.post(
        "/process",
        json={
            "carrier": "DHL",
            "statuses": [
                "Shipment in transit",
                "Out for delivery",
                "Shipment delivered",
            ],
            "mapping_file_path": str(mapping_file),
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["carrier"] == "DHL"
    assert payload["validation"] == "VALID"
    assert payload["validation_reason"] is None
    assert payload["current_status"] == "DELIVERED"
    assert payload["outcome"] == "SUCCESS"
    assert payload["mapped_statuses"] == 3
    assert payload["unmapped_statuses"] == 0


def test_process_missing_mapping_file():
    response = client.post(
        "/process",
        json={
            "carrier": "DHL",
            "statuses": [
                "Shipment delivered",
            ],
            "mapping_file_path": "missing-file.json",
        },
    )

    assert response.status_code == 400
    assert "Mapping file not found" in response.json()["detail"]