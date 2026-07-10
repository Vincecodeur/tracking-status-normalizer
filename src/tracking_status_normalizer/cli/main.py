"""
Command line interface entry point.
"""

import argparse

from tracking_status_normalizer.cli.commands import (
    governance_command,
    process_command,
)


DEFAULT_MAPPING_FILE = "data/mappings/carrier_status_mapping.json"


def build_parser() -> argparse.ArgumentParser:
    """
    Build the CLI argument parser.

    Returns:
        Configured argparse parser.
    """

    parser = argparse.ArgumentParser(
        prog="tsn",
        description=(
            "Tracking Status Normalizer command line interface."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    process_parser = subparsers.add_parser(
        "process",
        help="Process a shipment JSON file.",
    )

    process_parser.add_argument(
        "shipment_file",
        help="Path to the shipment JSON file.",
    )

    process_parser.add_argument(
        "--mapping",
        default=DEFAULT_MAPPING_FILE,
        help=(
            "Path to the carrier mapping JSON file. "
            f"Default: {DEFAULT_MAPPING_FILE}"
        ),
    )

    governance_parser = subparsers.add_parser(
        "governance",
        help="Run governance analysis.",
    )

    governance_parser.add_argument(
        "--format",
        choices=[
            "json",
            "markdown",
            "csv",
            "html",
        ],
        default="markdown",
        help="Output format.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """
    CLI main entry point.

    Args:
        argv:
            Optional list of command line arguments.
            Useful for tests.

    Returns:
        Exit code.
    """

    parser = build_parser()

    args = parser.parse_args(argv)

    if args.command == "process":
        return process_command(
            shipment_file_path=args.shipment_file,
            mapping_file_path=args.mapping,
        )

    if args.command == "governance":
        return governance_command(
            output_format=args.format,
        )

    parser.print_help()

    return 1