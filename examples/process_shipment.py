"""
Example: process a shipment.
"""

from pathlib import Path

from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)
from tracking_status_normalizer.processing.shipment_processor import (
    process_shipment,
)

registry = load_mapping_file(
    Path("data/mappings/carrier_status_mapping.json")
)

result = process_shipment(
    carrier="DHL",
    statuses=[
        "Shipment in transit",
        "Out for delivery",
        "Shipment delivered",
    ],
    mapping_registry=registry,
)

print("=== Shipment Result ===")
print()

print(f"Validation: {result.validation.valid}")

print(
    f"Current Status: "
    f"{result.lifecycle.current_status.value}"
)

print(
    f"Outcome: "
    f"{result.lifecycle.current_outcome.value}"
)

print(
    f"Mapped Statuses: "
    f"{result.mapped_statuses}"
)

print(
    f"Unmapped Statuses: "
    f"{result.unmapped_statuses}"
)