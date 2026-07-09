"""
Coverage level definitions.

This module defines the possible coverage levels used by the
Operational Coverage Matrix.

A coverage level indicates how completely a logistics capability
is represented by the catalog.
"""

from enum import Enum


class CoverageLevel(str, Enum):
    """
    Coverage level.

    FULL:
        All required statuses are present.

    PARTIAL:
        Some required statuses are present.

    NONE:
        No required statuses are present.
    """

    FULL = "FULL"

    PARTIAL = "PARTIAL"

    NONE = "NONE"