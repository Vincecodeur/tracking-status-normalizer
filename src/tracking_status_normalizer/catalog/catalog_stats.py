"""
Catalog statistics model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CatalogStats:
    """
    Statistics about a carrier catalog.
    """

    carrier: str

    total_mappings: int

    unique_canonical_statuses: int