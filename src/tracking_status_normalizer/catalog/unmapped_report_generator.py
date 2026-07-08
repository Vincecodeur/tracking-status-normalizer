"""
Unmapped report generator.
"""

from tracking_status_normalizer.catalog.unmapped_report import (
    UnmappedReport,
    UnmappedStatus,
)


def generate_unmapped_report(
    unknown_statuses: dict[tuple[str, str], int],
) -> UnmappedReport:
    """
    Build a report from unknown statuses.
    """

    results: list[UnmappedStatus] = []

    for (
        carrier,
        raw_status,
    ), count in unknown_statuses.items():

        results.append(
            UnmappedStatus(
                carrier=carrier,
                raw_status=raw_status,
                occurrences=count,
            )
        )

    results.sort(
        key=lambda status: status.occurrences,
        reverse=True,
    )

    return UnmappedReport(
        total_unknown_statuses=len(results),
        statuses=results,
    )