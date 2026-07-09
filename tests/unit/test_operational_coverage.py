"""
Tests for operational coverage analysis.
"""

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.coverage.capability import (
    Capability,
)
from tracking_status_normalizer.governance.coverage.coverage_level import (
    CoverageLevel,
)
from tracking_status_normalizer.governance.coverage.operational_coverage import (
    evaluate_operational_coverage,
)


def get_result(results, capability):
    """
    Return the coverage result for a capability.
    """

    return next(
        result
        for result in results
        if result.capability == capability
    )


def test_direct_delivery_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
            CanonicalStatus.DELIVERED,
        }
    )

    result = get_result(
        results,
        Capability.DIRECT_DELIVERY,
    )

    assert result.level == CoverageLevel.FULL


def test_direct_delivery_partial():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
        }
    )

    result = get_result(
        results,
        Capability.DIRECT_DELIVERY,
    )

    assert result.level == CoverageLevel.PARTIAL

    assert result.missing_statuses == [
        CanonicalStatus.DELIVERED,
    ]


def test_direct_delivery_none():
    results = evaluate_operational_coverage(set())

    result = get_result(
        results,
        Capability.DIRECT_DELIVERY,
    )

    assert result.level == CoverageLevel.NONE


def test_returns_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.RETURN_INITIATED,
            CanonicalStatus.RETURN_IN_TRANSIT,
            CanonicalStatus.RETURN_DELIVERED,
        }
    )

    result = get_result(
        results,
        Capability.RETURNS,
    )

    assert result.level == CoverageLevel.FULL


def test_returns_partial():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.RETURN_INITIATED,
            CanonicalStatus.RETURN_IN_TRANSIT,
        }
    )

    result = get_result(
        results,
        Capability.RETURNS,
    )

    assert result.level == CoverageLevel.PARTIAL

    assert result.missing_statuses == [
        CanonicalStatus.RETURN_DELIVERED,
    ]


def test_returns_none():
    results = evaluate_operational_coverage(set())

    result = get_result(
        results,
        Capability.RETURNS,
    )

    assert result.level == CoverageLevel.NONE


def test_pudo_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKUP_EXPIRED,
        }
    )

    result = get_result(
        results,
        Capability.PUDO,
    )

    assert result.level == CoverageLevel.FULL


def test_locker_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.DELIVERED_TO_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKED_UP_BY_CUSTOMER,
        }
    )

    result = get_result(
        results,
        Capability.LOCKER,
    )

    assert result.level == CoverageLevel.FULL


def test_out_of_home_full_from_pudo():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKUP_EXPIRED,
        }
    )

    result = get_result(
        results,
        Capability.OUT_OF_HOME_DELIVERY,
    )

    assert result.level == CoverageLevel.FULL


def test_out_of_home_full_from_locker():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.DELIVERED_TO_PICKUP_POINT,
            CanonicalStatus.AVAILABLE_FOR_PICKUP,
            CanonicalStatus.PICKED_UP_BY_CUSTOMER,
        }
    )

    result = get_result(
        results,
        Capability.OUT_OF_HOME_DELIVERY,
    )

    assert result.level == CoverageLevel.FULL


def test_out_of_home_partial():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.ARRIVED_AT_PICKUP_POINT,
        }
    )

    result = get_result(
        results,
        Capability.OUT_OF_HOME_DELIVERY,
    )

    assert result.level == CoverageLevel.PARTIAL


def test_out_of_home_none():
    results = evaluate_operational_coverage(set())

    result = get_result(
        results,
        Capability.OUT_OF_HOME_DELIVERY,
    )

    assert result.level == CoverageLevel.NONE


def test_customs_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.CUSTOMS_PROCESSING,
        }
    )

    result = get_result(
        results,
        Capability.CUSTOMS,
    )

    assert result.level == CoverageLevel.FULL


def test_exception_management_full():
    results = evaluate_operational_coverage(
        {
            CanonicalStatus.EXCEPTION,
            CanonicalStatus.LOST,
            CanonicalStatus.DAMAGED,
            CanonicalStatus.HELD,
        }
    )

    result = get_result(
        results,
        Capability.EXCEPTION_MANAGEMENT,
    )

    assert result.level == CoverageLevel.FULL


def test_capability_order():
    results = evaluate_operational_coverage(set())

    capabilities = [
        result.capability
        for result in results
    ]

    assert capabilities == [
        Capability.DIRECT_DELIVERY,
        Capability.PUDO,
        Capability.LOCKER,
        Capability.OUT_OF_HOME_DELIVERY,
        Capability.RETURNS,
        Capability.CUSTOMS,
        Capability.EXCEPTION_MANAGEMENT,
    ]