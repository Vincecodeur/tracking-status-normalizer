"""
Capability definitions.

This module defines the canonical statuses required
for each logistics capability.

Capability definitions are the foundation of the
Operational Coverage Matrix.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)


@dataclass(frozen=True)
class CapabilityDefinition:
    """
    Logistics capability definition.

    Attributes:
        capability:
            Capability being defined.

        required_statuses:
            Canonical statuses required to achieve FULL coverage.
    """

    capability: Capability

    required_statuses: list[CanonicalStatus]


CAPABILITY_DEFINITIONS: dict[
    Capability,
    CapabilityDefinition,
] = {
    Capability.DIRECT_DELIVERY: CapabilityDefinition(
        capability=Capability.DIRECT_DELIVERY,
        required_statuses=[
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
            CanonicalStatus.DELIVERED,
        ],
    ),
    Capability.PUDO: CapabilityDefinition(
        capability=Capability.PUDO,
        required_statuses=[
            CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKUP_EXPIRED,
        ],
    ),
    Capability.LOCKER: CapabilityDefinition(
        capability=Capability.LOCKER,
        required_statuses=[
            CanonicalStatus.DELIVERED_TO_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKED_UP_BY_CUSTOMER,
        ],
    ),
    Capability.RETURNS: CapabilityDefinition(
        capability=Capability.RETURNS,
        required_statuses=[
            CanonicalStatus.RETURN_INITIATED,
            CanonicalStatus.RETURN_IN_TRANSIT,
            CanonicalStatus.RETURN_DELIVERED,
        ],
    ),
    Capability.CUSTOMS: CapabilityDefinition(
        capability=Capability.CUSTOMS,
        required_statuses=[
            CanonicalStatus.CUSTOMS_PROCESSING,
        ],
    ),
    Capability.EXCEPTION_MANAGEMENT: CapabilityDefinition(
        capability=Capability.EXCEPTION_MANAGEMENT,
        required_statuses=[
            CanonicalStatus.EXCEPTION,
            CanonicalStatus.LOST,
            CanonicalStatus.DAMAGED,
            CanonicalStatus.HELD,
        ],
    ),
}