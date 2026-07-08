"""
Shipment file loader.
"""

import json
from pathlib import Path

from tracking_status_normalizer.io.shipment_file import (
    ShipmentFile,
)


def load_shipment_file(
    file_path: str | Path,
) -> ShipmentFile:
    """
    Load a shipment file from JSON.

    Expected format:

    {
        "carrier": "DHL",
        "statuses": [
            "Shipment in transit",
            "Shipment delivered"
        ]
    }
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Shipment file not found: {path}"
        )

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        content = json.load(file)

    if "carrier" not in content:
        raise ValueError(
            "Missing required field: carrier"
        )

    if "statuses" not in content:
        raise ValueError(
            "Missing required field: statuses"
        )

    if not isinstance(content["statuses"], list):
        raise ValueError(
            "statuses must be a list"
        )

    return ShipmentFile(
        carrier=content["carrier"],
        statuses=content["statuses"],
    )