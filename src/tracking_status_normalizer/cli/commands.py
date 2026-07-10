"""
CLI command implementations.

This module contains the actual business actions called by the command line
interface.
"""

from pathlib import Path

from tracking_status_normalizer.cli.governance_cli import (
    build_governance_report_from_statuses,
)
from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.governance.exporters.csv_exporter import (
    export_summary_to_csv,
)
from tracking_status_normalizer.governance.exporters.html_exporter import (
    export_to_html,
)
from tracking_status_normalizer.governance.exporters.json_exporter import (
    export_to_json,
)
from tracking_status_normalizer.governance.exporters.markdown_exporter import (
    export_to_markdown,
)
from tracking_status_normalizer.io.shipment_loader import (
    load_shipment_file,
)
from tracking_status_normalizer.normalization.mapping_loader import (
    load_mapping_file,
)
from tracking_status_normalizer.processing.shipment_processor import (
    process_shipment,
)


def process_command(
    shipment_file_path: str,
    mapping_file_path: str,
) -> int:
    """
    Process a shipment JSON file.

    Args:
        shipment_file_path:
            Path to the shipment JSON file.

        mapping_file_path:
            Path to the carrier mapping JSON file.

    Returns:
        Exit code:
        - 0 for successful execution
        - 1 for unexpected processing failure
    """

    try:
        shipment = load_shipment_file(
            Path(shipment_file_path)
        )

        mapping_registry = load_mapping_file(
            Path(mapping_file_path)
        )

        result = process_shipment(
            carrier=shipment.carrier,
            statuses=shipment.statuses,
            mapping_registry=mapping_registry,
        )

    except Exception as error:
        print("ERROR")
        print("-----")
        print(str(error))
        return 1

    validation_status = (
        "VALID"
        if result.validation.valid
        else "INVALID"
    )

    print("=" * 50)
    print("Tracking Status Normalizer")
    print("=" * 50)
    print()
    print(f"Carrier           : {shipment.carrier}")
    print(f"Validation        : {validation_status}")

    if not result.validation.valid:
        print(f"Reason            : {result.validation.reason}")

    print(
        f"Current Status    : "
        f"{result.lifecycle.current_status.value}"
    )

    print(
        f"Outcome           : "
        f"{result.lifecycle.current_outcome.value}"
    )

    print(f"Mapped Statuses   : {result.mapped_statuses}")
    print(f"Unmapped Statuses : {result.unmapped_statuses}")

    return 0


def governance_command(
    output_format: str,
) -> int:
    """
    Run governance analysis.

    Args:
        output_format:
            Export format.

    Returns:
        Exit code.
    """

    try:
        statuses = {
            CanonicalStatus.IN_TRANSIT,
            CanonicalStatus.OUT_FOR_DELIVERY,
            CanonicalStatus.DELIVERED,
            CanonicalStatus.EXCEPTION,
            CanonicalStatus.LOST,
            CanonicalStatus.DAMAGED,
            CanonicalStatus.HELD,
        }

        report = (
            build_governance_report_from_statuses(
                statuses
            )
        )

        if output_format == "json":
            output = export_to_json(
                report
            )

        elif output_format == "markdown":
            output = export_to_markdown(
                report
            )

        elif output_format == "csv":
            output = export_summary_to_csv(
                report
            )

        elif output_format == "html":
            output = export_to_html(
                report
            )

        else:
            print(
                f"Unsupported format: "
                f"{output_format}"
            )
            return 1

        print(output)

        return 0

    except Exception as error:
        print("ERROR")
        print("-----")
        print(str(error))
        return 1