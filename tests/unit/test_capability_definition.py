from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.capability_definition import (
    CAPABILITY_DEFINITIONS,
)


def test_direct_delivery_definition():
    definition = CAPABILITY_DEFINITIONS[
        Capability.DIRECT_DELIVERY
    ]

    assert definition.required_statuses == [
        CanonicalStatus.IN_TRANSIT,
        CanonicalStatus.OUT_FOR_DELIVERY,
        CanonicalStatus.DELIVERED,
    ]