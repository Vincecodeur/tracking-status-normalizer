"""
Example: load and process a shipment file.
"""

from pathlib import Path

from tracking_status_normalizer.io.shipment_loader import (
    load_shipment_file,
)
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)
from tracking_status_normalizer.processing.shipment_processor import (
    process_shipment,
)

shipment = load_shipment_file(
    Path(
        "examples/data/dhl_delivery.json"
    )
)

registry = load_mapping_file(
    Path(
        "data/mappings/carrier_status_mapping.json"
    )
)

result = process_shipment(
    carrier=shipment.carrier,
    statuses=shipment.statuses,
    mapping_registry=registry,
)

print(result)