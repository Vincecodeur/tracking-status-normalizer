# Domain Model

Version: 1.0  
Status: Approved  
Epic: EPIC-003 – Domain Model

---

# Purpose

This document defines the core domain model of the Tracking Status Normalizer project.

The objective is to identify the business entities, their responsibilities, and their relationships before implementation.

The model is intentionally independent from any specific carrier, programming language, API, database, or user interface.

---

# Domain Overview

The project transforms carrier-specific tracking events into a standardized and validated tracking language.

```text
Carrier Event
      ↓
Carrier Status
      ↓
Mapping Rule
      ↓
Canonical Status
      ↓
Validation
      ↓
Business Outcome
```

---

# Domain Principles

## Canonical First

All carrier statuses must be translated into a canonical status.

The canonical status is the authoritative business representation.

---

## Immutable Core

Core entities are maintained by the project.

Users may extend the model without modifying the canonical taxonomy.

---

## Carrier Agnostic

The model must support:

- Postal operators
- Express carriers
- Parcel carriers
- Pickup point operators
- Locker networks
- Return logistics providers

---

# Entity: StatusCategory

## Purpose

Groups canonical statuses into business lifecycle phases.

Examples:

```text
TRANSIT
LAST_MILE
RETURN
EXCEPTION
```

---

## Responsibilities

- Organize canonical statuses
- Support reporting aggregation
- Support business workflows
- Support KPI calculations

---

## Attributes

| Attribute   | Type   |
| ----------- | ------ |
| name        | string |
| description | string |

---

# Entity: ShipmentOutcome

## Purpose

Represents the final business result of a shipment.

Examples:

```text
SUCCESS
RETURNED
FAILED
```
