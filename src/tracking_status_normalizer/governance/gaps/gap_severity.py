"""
Gap severity definitions.
"""

from enum import Enum


class GapSeverity(str, Enum):
    """
    Gap severity level.

    CRITICAL:
        Missing status affects a CORE capability.

    MEDIUM:
        Missing status significantly affects coverage.

    LOW:
        Missing status has limited operational impact.
    """

    CRITICAL = "CRITICAL"

    MEDIUM = "MEDIUM"

    LOW = "LOW"