"""
Example: analyze a lifecycle.
"""

from tracking_status_normalizer.analysis.lifecycle_analyzer import (
    analyze_lifecycle,
)
from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)

summary = analyze_lifecycle(
    [
        CanonicalStatus.IN_TRANSIT,
        CanonicalStatus.OUT_FOR_DELIVERY,
        CanonicalStatus.DELIVERED,
    ]
)

print(summary)