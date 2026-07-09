"""
CSV exporters for governance reports.

This module exports individual sections of a GovernanceReport
to CSV strings.

CSV is intentionally split by report section because a GovernanceReport
contains heterogeneous data:
- summary
- operational coverage
- gaps
- recommendations

Keeping separate CSV exports makes the output easier to consume in
Excel, Power BI, or any reporting tool.
"""

import csv
from io import StringIO

from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def export_summary_to_csv(
    report: GovernanceReport,
) -> str:
    """
    Export governance summary to CSV.

    Returns:
        CSV string with readiness and maturity information.
    """

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "field",
            "value",
        ]
    )

    writer.writerow(
        [
            "readiness_level",
            report.readiness_result.level.value,
        ]
    )

    writer.writerow(
        [
            "maturity_score",
            report.maturity_result.score,
        ]
    )

    writer.writerow(
        [
            "maturity_level",
            report.maturity_result.level.value,
        ]
    )

    return output.getvalue()


def export_coverage_to_csv(
    report: GovernanceReport,
) -> str:
    """
    Export operational coverage results to CSV.

    Returns:
        CSV string containing one row per capability.
    """

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "capability",
            "coverage_level",
            "required_statuses",
            "covered_statuses",
            "missing_statuses",
        ]
    )

    for result in report.coverage_results:

        missing_statuses = ";".join(
            status.value
            for status in result.missing_statuses
        )

        writer.writerow(
            [
                result.capability.value,
                result.level.value,
                result.required_statuses,
                result.covered_statuses,
                missing_statuses,
            ]
        )

    return output.getvalue()


def export_gaps_to_csv(
    report: GovernanceReport,
) -> str:
    """
    Export gaps to CSV.

    Returns:
        CSV string containing one row per gap.
    """

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "capability",
            "missing_status",
            "severity",
        ]
    )

    for gap in report.gaps:

        writer.writerow(
            [
                gap.capability.value,
                gap.missing_status.value,
                gap.severity.value,
            ]
        )

    return output.getvalue()


def export_recommendations_to_csv(
    report: GovernanceReport,
) -> str:
    """
    Export recommendations to CSV.

    Returns:
        CSV string containing one row per recommendation.
    """

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "priority",
            "capability",
            "message",
        ]
    )

    for recommendation in report.recommendations:

        writer.writerow(
            [
                recommendation.priority.value,
                recommendation.capability.value,
                recommendation.message,
            ]
        )

    return output.getvalue()