"""
CLI command implementations.

This module contains the actual business actions called by the command line
interface.
"""

from pathlib import Path

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