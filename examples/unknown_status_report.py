"""
Example: generate unknown status report.
"""

from tracking_status_normalizer.catalog.unmapped_report_generator import (
    generate_unmapped_report,
)
from tracking_status_normalizer.normalization.unknown_status_detector import (
    UnknownStatusDetector,
)

detector = UnknownStatusDetector()

detector.register(
    "DHL",
    "Delivered to neighbour",
)

detector.register(
    "DHL",
    "Delivered to neighbour",
)

detector.register(
    "UPS",
    "Customer requested hold",
)

report = generate_unmapped_report(
    detector.get_unknown_statuses()
)

print(report)