"""
Mapping rule definition.
"""

from dataclasses import dataclass

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)


@dataclass(frozen=True)
class MappingRule:
    """
    Maps a raw carrier status to a canonical status.
    """

    carrier: str
    raw_value: str
    canonical_status: CanonicalStatus