"""
Example: analyze catalog coverage.
"""

from pathlib import Path

from tracking_status_normalizer.normalization.coverage_analyzer import (
    analyze_coverage,
)
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)

registry = load_mapping_file(
    Path("data/mappings/carrier_status_mapping.json")
)

result = analyze_coverage(
    carrier="DHL",
    statuses=[
        "Shipment delivered",
        "Shipment in transit",
        "Unknown status",
    ],
    mapping_registry=registry,
)

print(result)