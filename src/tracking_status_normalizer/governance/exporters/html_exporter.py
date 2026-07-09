"""
HTML exporter.
"""

from tracking_status_normalizer.governance.exporters.markdown_exporter import (
    export_to_markdown,
)
from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def export_to_html(
    report: GovernanceReport,
) -> str:
    """
    Export governance report to HTML.
    """

    markdown = export_to_markdown(
        report
    )

    html = markdown.replace(
        "\n",
        "<br>\n",
    )

    return (
        "<html><body>"
        f"{html}"
        "</body></html>"
    )