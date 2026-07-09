"""
Gap model.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.gaps.gap_severity import (
    GapSeverity,
)


@dataclass(frozen=True)
class Gap:
    """
    Gap identified in a catalog.
    """

    capability: Capability

    missing_status: CanonicalStatus

    severity: GapSeverity