"""
Operational coverage analysis.

This module evaluates which logistics capabilities are covered
by a set of available canonical statuses.

It is the foundation of the Governance Layer.

The analyzer produces CoverageResult objects that are later used by:

- Readiness Assessment
- Gap Analysis
- Recommendation Engine
- Maturity Score
- Governance Reports
"""

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.capability_definition import (
    CAPABILITY_DEFINITIONS,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.coverage_result import (
    CoverageResult,
)


CAPABILITY_ORDER = [
    Capability.DIRECT_DELIVERY,
    Capability.PUDO,
    Capability.LOCKER,
    Capability.OUT_OF_HOME_DELIVERY,
    Capability.RETURNS,
    Capability.CUSTOMS,
    Capability.EXCEPTION_MANAGEMENT,
]


def evaluate_operational_coverage(
    available_statuses: set[CanonicalStatus],
) -> list[CoverageResult]:
    """
    Evaluate operational coverage.

    Args:
        available_statuses:
            Canonical the catalog.

    Returns:
        Ordered list of coverage results.
    """

    results: dict[
        Capability,
        CoverageResult,
    ] = {}

    for capability, definition in (
        CAPABILITY_DEFINITIONS.items()
    ):
        required_statuses = definition.required_statuses

        covered_statuses = [
            status
            for status in required_statuses
            if status in available_statuses
        ]

        missing_statuses = [
            status
            for status in required_statuses
            if status not in available_statuses
        ]

        level = _determine_coverage_level(
            required_count=len(required_statuses),
            covered_count=len(covered_statuses),
        )

        results[capability] = CoverageResult(
            capability=capability,
            level=level,
            required_statuses=len(required_statuses),
            covered_statuses=len(covered_statuses),
            missing_statuses=missing_statuses,
        )

    results[
        Capability.OUT_OF_HOME_DELIVERY
    ] = _calculate_out_of_home_delivery(
        results,
    )

    return [
        results[capability]
        for capability in CAPABILITY_ORDER
    ]


def _determine_coverage_level(
    required_count: int,
    covered_count: int,
) -> CoverageLevel:
    """
    Determine coverage level.

    Args:
        required_count:
            Number of required statuses.

        covered_count:
            Number of covered statuses.

    Returns:
        Coverage level.
    """

    if covered_count == 0:
        return CoverageLevel.NONE

    if covered_count == required_count:
        return CoverageLevel.FULL

    return CoverageLevel.PARTIAL


def _calculate_out_of_home_delivery(
    results: dict[
        Capability,
        CoverageResult,
    ],
) -> CoverageResult:
    """
    Calculate the derived OUT_OF_HOME_DELIVERY capability.

    Rules:

    FULL:
        PUDO is FULL
        OR
        LOCKER is FULL

    PARTIAL:
        PUDO is PARTIAL
        OR
        LOCKER is PARTIAL

    NONE:
        PUDO is NONE
        AND
        LOCKER is NONE
    """

    pudo_level = results[
        Capability.PUDO
    ].level

    locker_level = results[
        Capability.LOCKER
    ].level

    if (
        pudo_level == CoverageLevel.FULL
        or locker_level == CoverageLevel.FULL
    ):
        level = CoverageLevel.FULL

    elif (
        pudo_level == CoverageLevel.PARTIAL
        or locker_level == CoverageLevel.PARTIAL
    ):
        level = CoverageLevel.PARTIAL

    else:
        level = CoverageLevel.NONE

    return CoverageResult(
        capability=Capability.OUT_OF_HOME_DELIVERY,
        level=level,
        required_statuses=0,
        covered_statuses=0,
        missing_statuses=[],
    )