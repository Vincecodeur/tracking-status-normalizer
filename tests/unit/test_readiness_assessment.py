"""
Tests for readiness assessment.
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
from tracking_status_normalizer.governance.readiness.readiness_assessment import (
    assess_readiness,
)
from tracking_status_normalizer.governance.readiness.readiness_level import (
    ReadinessLevel,
)


def make_result(
    capability,
    level,
):
    """
    Build a simplified CoverageResult for readiness tests.
    """

    return CoverageResult(
        capability=capability,
        level=level,
        required_statuses=0,
        covered_statuses=0,
        missing_statuses=[],
    )


def test_readiness_go_when_all_capabilities_full():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.RETURNS,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.CUSTOMS,
            CoverageLevel.FULL,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.GO

    assert readiness.blocking_capabilities == []

    assert readiness.risk_capabilities == []

    assert readiness.reasons == []


def test_readiness_go_with_risks_when_extended_capability_is_none():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.RETURNS,
            CoverageLevel.NONE,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.GO_WITH_RISKS

    assert readiness.blocking_capabilities == []

    assert readiness.risk_capabilities == [
        Capability.RETURNS,
    ]

    assert readiness.reasons == [
        "RETURNS is NONE.",
    ]


def test_readiness_go_with_risks_when_extended_capability_is_partial():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.PUDO,
            CoverageLevel.PARTIAL,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.GO_WITH_RISKS

    assert readiness.blocking_capabilities == []

    assert readiness.risk_capabilities == [
        Capability.PUDO,
    ]

    assert readiness.reasons == [
        "PUDO is PARTIAL.",
    ]


def test_readiness_no_go_when_direct_delivery_is_partial():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.PARTIAL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.NO_GO

    assert readiness.blocking_capabilities == [
        Capability.DIRECT_DELIVERY,
    ]

    assert readiness.risk_capabilities == []

    assert readiness.reasons == [
        "DIRECT_DELIVERY is PARTIAL.",
    ]


def test_readiness_no_go_when_direct_delivery_is_none():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.NONE,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.NO_GO

    assert readiness.blocking_capabilities == [
        Capability.DIRECT_DELIVERY,
    ]

    assert readiness.reasons == [
        "DIRECT_DELIVERY is NONE.",
    ]


def test_readiness_no_go_when_exception_management_is_partial():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.PARTIAL,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.NO_GO

    assert readiness.blocking_capabilities == [
        Capability.EXCEPTION_MANAGEMENT,
    ]

    assert readiness.reasons == [
        "EXCEPTION_MANAGEMENT is PARTIAL.",
    ]


def test_readiness_no_go_when_exception_management_is_none():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.NONE,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.NO_GO

    assert readiness.blocking_capabilities == [
        Capability.EXCEPTION_MANAGEMENT,
    ]

    assert readiness.reasons == [
        "EXCEPTION_MANAGEMENT is NONE.",
    ]


def test_readiness_no_go_has_priority_over_risks():
    results = [
        make_result(
            Capability.DIRECT_DELIVERY,
            CoverageLevel.NONE,
        ),
        make_result(
            Capability.EXCEPTION_MANAGEMENT,
            CoverageLevel.FULL,
        ),
        make_result(
            Capability.RETURNS,
            CoverageLevel.NONE,
        ),
    ]

    readiness = assess_readiness(
        results
    )

    assert readiness.level == ReadinessLevel.NO_GO

    assert readiness.blocking_capabilities == [
        Capability.DIRECT_DELIVERY,
    ]

    assert readiness.risk_capabilities == [
        Capability.RETURNS,
    ]

    assert readiness.reasons == [
        "DIRECT_DELIVERY is NONE.",
        "RETURNS is NONE.",
    ]