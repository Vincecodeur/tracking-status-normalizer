# CLI Guide

## Process a Shipment

Process a shipment file using the default mapping catalog.

Example:

tsn process shipment.json

---

## Process a Shipment with a Custom Mapping File

Example:

tsn process shipment.json --mapping custom_mapping.json

---

## Governance Report

Generate a governance report.

Markdown:

tsn governance

or

tsn governance --format markdown

---

JSON:

tsn governance --format json

---

CSV:

tsn governance --format csv

---

HTML:

tsn governance --format html

---

## Exit Codes

0
Success

1
Processing error
