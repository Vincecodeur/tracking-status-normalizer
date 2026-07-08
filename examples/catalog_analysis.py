"""
Example: analyze catalog.
"""

from pathlib import Path

from tracking_status_normalizer.catalog.catalog_analyzer import (
    analyze_catalog,
)
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)

registry = load_mapping_file(
    Path("data/mappings/carrier_status_mapping.json")
)

stats = analyze_catalog(
    carrier="DHL",
    mapping_registry=registry,
)

print(stats)