"""
Readiness assessment result.
"""

from dataclasses import dataclass

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)


@dataclass(frozen=True)
class ReadinessResult:
    """
    Readiness assessment result.

    Attributes:
        level:
            Readiness level.

        blocking_capabilities:
            CORE capabilities causing a NO_GO assessment.

        risk_capabilities:
            EXTENDED capabilities causing a
            GO_WITH_RISKS assessment.

        reasons:
            Human-readable explanations.
    """

    level: ReadinessLevel

    blocking_capabilities: list[Capability]

    risk_capabilities: list[Capability]

    reasons: list[str]