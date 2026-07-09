"""
Maturity result model.
"""

from dataclasses import dataclass

from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)


@dataclass(frozen=True)
class MaturityResult:
    """
    Catalog maturity assessment result.
    """

    score: int

    level: MaturityLevel

    reasons: list[str]