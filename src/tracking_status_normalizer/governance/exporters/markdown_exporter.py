"""
Markdown exporter.
"""

from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def export_to_markdown(
    report: GovernanceReport,
) -> str:
    """
    Export governance report to Markdown.
    """

    lines = []

    lines.append("# Governance Report")
    lines.append("")

    lines.append("## Readiness")
    lines.append(
        f"- Level: {report.readiness_result.level.value}"
    )
    lines.append("")

    lines.append("## Maturity")
    lines.append(
        f"- Score: {report.maturity_result.score}"
    )
    lines.append(
        f"- Level: {report.maturity_result.level.value}"
    )
    lines.append("")

    lines.append("## Coverage")

    for result in report.coverage_results:

        lines.append(
            f"- {result.capability.value}: "
            f"{result.level.value}"
        )

    lines.append("")

    lines.append("## Gaps")

    if not report.gaps:

        lines.append("- None")

    else:

        for gap in report.gaps:

            lines.append(
                f"- {gap.missing_status.value} "
                f"({gap.severity.value})"
            )

    lines.append("")

    lines.append("## Recommendations")

    if not report.recommendations:

        lines.append("- None")

    else:

        for recommendation in report.recommendations:

            lines.append(
                f"- [{recommendation.priority.value}] "
                f"{recommendation.message}"
            )

    return "\n".join(lines)