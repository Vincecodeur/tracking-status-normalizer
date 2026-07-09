"""
Coverage result model.

This module defines the result of a capability coverage evaluation.

A CoverageResult describes how well a specific logistics capability
is represented by a carrier catalog.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)


@dataclass(frozen=True)
class CoverageResult:
    """
    Coverage evaluation result.

    Attributes:
        capability:
            Evaluated logistics capability.

        level:
            Coverage level.

        required_statuses:
            Number of statuses required by the capability.

        covered_statuses:
            Number of required statuses currently covered.

        missing_statuses:
            Required statuses that are not covered.
    """

    capability: Capability

    level: CoverageLevel

    required_statuses: int

    covered_statuses: int

    missing_statuses: list[CanonicalStatus]