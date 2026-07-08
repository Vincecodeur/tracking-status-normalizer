"""
Example: normalize a carrier status.
"""

from pathlib import Path

from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)
from tracking_status_normalizer.normalization.normalizer import (
    normalize,
)

registry = load_mapping_file(
    Path("data/mappings/carrier_status_mapping.json")
)

result = normalize(
    carrier="DHL",
    raw_status="Shipment delivered",
    mapping_registry=registry,
)

print(result)