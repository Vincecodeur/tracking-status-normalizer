"""
Mapping loader.

This module loads carrier-to-canonical status mappings from a JSON file.
"""

import json
from pathlib import Path

from tracking_status_normalizer.domain.canonical_status import CanonicalStatus
from tracking_status_normalizer.normalization.text_normalizer import (
    normalize_text,
)


MappingRegistry = dict[tuple[str, str], CanonicalStatus]


def load_mapping_file(file_path: str | Path) -> MappingRegistry:
    """
    Load carrier status mappings from a JSON file.

    Args:
        file_path: Path to the mapping JSON file.

    Returns:
        A dictionary using normalized carrier and status as lookup key.

    Raises:
        FileNotFoundError: If the mapping file does not exist.
        ValueError: If the JSON structure is invalid.
        ValueError: If a canonical status is unknown.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Mapping file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        content = json.load(file)

    if "mappings" not in content:
        raise ValueError("Mapping file must contain a 'mappings' key.")

    registry: MappingRegistry = {}

    for item in content["mappings"]:
        carrier = item.get("carrier")
        raw_status = item.get("raw_status")
        canonical_status = item.get("canonical_status")

        if not carrier or not raw_status or not canonical_status:
            raise ValueError(
                "Each mapping must contain carrier, raw_status, and canonical_status."
            )

        try:
            canonical = CanonicalStatus(canonical_status)
        except ValueError as error:
            raise ValueError(
                f"Unknown canonical status: {canonical_status}"
            ) from error

        key = (
            normalize_text(carrier),
            normalize_text(raw_status),
        )

        registry[key] = canonical

    return registry