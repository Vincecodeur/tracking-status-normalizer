"""
Example: validate a lifecycle.
"""

from tracking_status_normalizer.domain.canonical_status import (
    CanonicalStatus,
)
from tracking_status_normalizer.validation.lifecycle_validator import (
    validate_lifecycle,
)

result = validate_lifecycle(
    [
        CanonicalStatus.IN_TRANSIT,
        CanonicalStatus.OUT_FOR_DELIVERY,
        CanonicalStatus.DELIVERED,
    ]
)

print(result)