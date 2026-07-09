"""
Capability registry.

Provides access to capability definitions.
"""

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.capability_definition import (
    CAPABILITY_DEFINITIONS,
    CapabilityDefinition,
)


def get_capability_definition(
    capability: Capability,
) -> CapabilityDefinition:
    """
    Return a capability definition.
    """

    return CAPABILITY_DEFINITIONS[capability]
