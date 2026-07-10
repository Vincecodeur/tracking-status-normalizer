"""
Tests for governance CLI orchestration.
"""

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)

from tracking_status_normalizer.cli.governance_cli import (
    build_governance_report_from_statuses,
)



def test_build_complete_governance_report():
    report = (
        build_governance_report_from_statuses(
            {
                CanonicalStatus.IN_TRANSIT,
                CanonicalStatus.OUT_FOR_DELIVERY,
                CanonicalStatus.DELIVERED,
                CanonicalStatus.EXCEPTION,
                CanonicalStatus.LOST,
                CanonicalStatus.DAMAGED,
                CanonicalStatus.HELD,
            }
        )
    )

    assert report is not None

    assert report.readiness_result is not None

    assert report.maturity_result is not None

    assert len(report.coverage_results) > 0


def test_governance_report_contains_readiness():
    report = (
        build_governance_report_from_statuses(
            {
                CanonicalStatus.IN_TRANSIT,
                CanonicalStatus.OUT_FOR_DELIVERY,
                CanonicalStatus.DELIVERED,
                CanonicalStatus.EXCEPTION,
                CanonicalStatus.LOST,
                CanonicalStatus.DAMAGED,
                CanonicalStatus.HELD,
            }
        )
    )

    assert report.readiness_result is not None


def test_governance_report_contains_maturity():
    report = (
        build_governance_report_from_statuses(
            {
                CanonicalStatus.IN_TRANSIT,
                CanonicalStatus.OUT_FOR_DELIVERY,
                CanonicalStatus.DELIVERED,
                CanonicalStatus.EXCEPTION,
                CanonicalStatus.LOST,
                CanonicalStatus.DAMAGED,
                CanonicalStatus.HELD,
            }
        )
    )

    assert report.maturity_result is not None


def test_governance_report_contains_coverage():
    report = (
        build_governance_report_from_statuses(
            {
                CanonicalStatus.IN_TRANSIT,
                CanonicalStatus.OUT_FOR_DELIVERY,
                CanonicalStatus.DELIVERED,
                CanonicalStatus.EXCEPTION,
                CanonicalStatus.LOST,
                CanonicalStatus.DAMAGED,
                CanonicalStatus.HELD,
            }
        )
    )

    assert len(report.coverage_results) > 0