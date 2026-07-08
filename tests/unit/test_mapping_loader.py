import json

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)


def test_load_valid_mapping_file(tmp_path):
    mapping_file = tmp_path / "mapping.json"

    mapping_file.write_text(
        json.dumps(
            {
                "mappings": [
                    {
                        "carrier": "DHL",
                        "raw_status": "Shipment delivered",
                        "canonical_status": "DELIVERED",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    registry = load_mapping_file(mapping_file)

    assert registry[("dhl", "shipment delivered")] == CanonicalStatus.DELIVERED


def test_load_mapping_with_unknown_canonical_status(tmp_path):
    mapping_file = tmp_path / "mapping.json"

    mapping_file.write_text(
        json.dumps(
            {
                "mappings": [
                    {
                        "carrier": "DHL",
                        "raw_status": "Shipment delivered",
                        "canonical_status": "UNKNOWN_STATUS",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    try:
        load_mapping_file(mapping_file)
    except ValueError as error:
        assert "Unknown canonical status" in str(error)
    else:
        assert False, "Expected ValueError for unknown canonical status."


def test_missing_mappings_key(tmp_path):
    mapping_file = tmp_path / "mapping.json"

    mapping_file.write_text(
        json.dumps({}),
        encoding="utf-8",
    )

    try:
        load_mapping_file(mapping_file)
    except ValueError as error:
        assert "mappings" in str(error)
    else:
        assert False, "Expected ValueError for missing mappings key."