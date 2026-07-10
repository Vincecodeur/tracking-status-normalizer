# Governance Layer Architecture

## Purpose

The Governance Layer evaluates the quality and completeness of a carrier catalog.

It does not perform normalization.

It analyzes the outputs produced by the Engine Layer.

---

## Governance Pipeline

Canonical Statuses
|
v
Operational Coverage
|
v
Readiness Assessment
|
v
Gap Analysis
|
v
Recommendations
|
v
Maturity Assessment
|
v
Governance Report
|
v
Exporters

---

## Coverage

Evaluates which operational capabilities are covered by the catalog.

Capabilities:

- DIRECT_DELIVERY
- PUDO
- LOCKER
- OUT_OF_HOME_DELIVERY
- RETURNS
- CUSTOMS
- EXCEPTION_MANAGEMENT

Coverage Levels:

- FULL
- PARTIAL
- NONE

---

## Readiness

Determines whether the catalog is operationally usable.

Readiness Levels:

- GO
- GO_WITH_RISKS
- NO_GO

---

## Gap Analysis

Identifies missing canonical statuses.

Gap Severity:

- CRITICAL
- MEDIUM
- LOW

---

## Recommendations

Maps gaps to concrete improvement actions.

Recommendation Priority:

- HIGH
- MEDIUM
- LOW

---

## Maturity

Provides a global assessment of catalog quality.

Maturity Levels:

- BASIC
- DEVELOPING
- MATURE
- ADVANCED

---

## Reporting

Aggregates all governance results into a single GovernanceReport object.
