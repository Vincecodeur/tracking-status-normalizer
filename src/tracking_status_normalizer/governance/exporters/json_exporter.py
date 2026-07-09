"""
JSON exporter.
"""

import json
from dataclasses import asdict

from tracking_status_normalizer.governance.reporting.governance_report import (
    GovernanceReport,
)


def export_to_json(
    report: GovernanceReport,
) -> str:
    """
    Export governance report to JSON.
    """

    return json.dumps(
        asdict(report),
        indent=4,
        default=str,
    )