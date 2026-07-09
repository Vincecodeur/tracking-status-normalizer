"""
Readiness assessment.

This module evaluates whether a catalog is operationally
ready based on Operational Coverage Results.
"""

from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)
from tracking_status_normalizer.governance.readiness.readiness_result import (
    ReadinessResult,
)


CORE_CAPABILITIES = {
    Capability.DIRECT_DELIVERY,
    Capability.EXCEPTION_MANAGEMENT,
}


def assess_readiness(
    coverage_results: list[CoverageResult],
) -> ReadinessResult:
    """
    Assess catalog readiness.

    Rules:

    GO:
        All CORE capabilities are FULL and all
        EXTENDED capabilities are FULL.

    GO_WITH_RISKS:
        All CORE capabilities are FULL but one
        or more EXTENDED capabilities are PARTIAL
        or NONE.

    NO_GO:
        One or more CORE capabilities are PARTIAL
        or NONE.
    """

    blocking_capabilities = []

    risk_capabilities = []

    reasons = []

    for result in coverage_results:

        if result.capability in CORE_CAPABILITIES:

            if result.level != CoverageLevel.FULL:

                blocking_capabilities.append(
                    result.capability
                )

                reasons.append(
                    f"{result.capability.value} "
                    f"is {result.level.value}."
                )

        else:

            if result.level != CoverageLevel.FULL:

                risk_capabilities.append(
                    result.capability
                )

                reasons.append(
                    f"{result.capability.value} "
                    f"is {result.level.value}."
                )

    if blocking_capabilities:

        level = ReadinessLevel.NO_GO

    elif risk_capabilities:

        level = ReadinessLevel.GO_WITH_RISKS

    else:

        level = ReadinessLevel.GO

    return ReadinessResult(
        level=level,
        blocking_capabilities=blocking_capabilities,
        risk_capabilities=risk_capabilities,
        reasons=reasons,
    )