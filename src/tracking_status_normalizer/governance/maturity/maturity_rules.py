"""
Maturity rules.
"""

from tracking_status_normalizer.governance.maturity.maturity_level import (
    MaturityLevel,
)


def determine_maturity_level(
    score: int,
) -> MaturityLevel:
    """
    Determine maturity level from score.
    """

    if score >= 90:
        return MaturityLevel.ADVANCED

    if score >= 70:
        return MaturityLevel.MATURE

    if score >= 50:
        return MaturityLevel.DEVELOPING

    return MaturityLevel.BASIC