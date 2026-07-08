"""
Text normalization helpers.

This module converts carrier names and raw statuses into stable lookup keys.
"""

import re
import unicodedata


def normalize_text(value: str) -> str:
    """
    Normalize a text value for reliable matching.

    The goal is to make carrier statuses easier to compare.

    Example:
        "Votre colis est livré."
        becomes
        "votre colis est livre"

    Steps:
        - Strip leading and trailing spaces
        - Convert to lowercase
        - Remove accents
        - Replace punctuation with spaces
        - Collapse repeated spaces
    """

    # Remove leading/trailing spaces and normalize case.
    normalized = value.strip().casefold()

    # Decompose accented characters.
    # Example: "é" becomes "e" + accent marker.
    normalized = unicodedata.normalize("NFKD", normalized)

    # Remove accent markers.
    normalized = "".join(
        character
        for character in normalized
        if not unicodedata.combining(character)
    )

    # Replace non-alphanumeric characters with spaces.
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)

    # Collapse repeated spaces into a single space.
    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()