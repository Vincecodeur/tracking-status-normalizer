"""
Mapping registry.

V1:
Hardcoded mappings.

V2:
CSV/YAML driven mappings.
"""

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)

MAPPING_REGISTRY = {
    # DHL
    ("dhl", "shipment delivered"):
        CanonicalStatus.DELIVERED,

    ("dhl", "shipment in transit"):
        CanonicalStatus.IN_TRANSIT,

    # UPS
    ("ups", "delivered"):
        CanonicalStatus.DELIVERED,

    ("ups", "on the way"):
        CanonicalStatus.IN_TRANSIT,

    # Colissimo
    ("colissimo", "votre colis est livré"):
        CanonicalStatus.DELIVERED,

    ("colissimo", "votre colis est en cours d acheminement"):
        CanonicalStatus.IN_TRANSIT,

    # Amazon Shipping
    ("amazon shipping", "package delivered"):
        CanonicalStatus.DELIVERED,

    ("amazon shipping", "package in transit"):
        CanonicalStatus.IN_TRANSIT,
}