"""
Unknown status detection.
"""

from collections import Counter


class UnknownStatusDetector:
    """
    Tracks unmapped statuses.
    """

    def __init__(self):
        self._statuses = Counter()

    def register(
        self,
        carrier: str,
        raw_status: str,
    ) -> None:
        """
        Store an unknown status.
        """

        key = (
            carrier,
            raw_status,
        )

        self._statuses[key] += 1

    def get_unknown_statuses(self):
        """
        Returns all discovered unmapped statuses.
        """

        return dict(self._statuses)