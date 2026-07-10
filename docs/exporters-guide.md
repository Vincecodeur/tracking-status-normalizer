# Exporters Guide

## Purpose

Exporters transform Governance Reports into portable formats.

Exporters never contain business logic.

They only expose information already calculated by the Governance Layer.

---

## JSON Exporter

Purpose:

Machine-readable output.

Example Usage:

export_to_json(report)

---

## Markdown Exporter

Purpose:

Human-readable reports.

Ideal for:

- GitHub
- Documentation
- Audit reports

Example Usage:

export_to_markdown(report)

---

## CSV Exporter

Purpose:

Excel and Power BI analysis.

Available CSV exports:

- Summary
- Coverage
- Gaps
- Recommendations

Example Usage:

export_summary_to_csv(report)

export_coverage_to_csv(report)

export_gaps_to_csv(report)

export_recommendations_to_csv(report)

---

## HTML Exporter

Purpose:

Lightweight web rendering.

Example Usage:

export_to_html(report)
