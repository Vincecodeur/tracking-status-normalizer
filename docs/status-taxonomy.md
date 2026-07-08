# Status Taxonomy

Version: 1.0  
Status: Approved  
Epic: EPIC-002 – Canonical Tracking Taxonomy

---

# Purpose

This document defines the canonical shipment tracking taxonomy used by the Tracking Status Normalizer project.

The objective is to provide a carrier-agnostic representation of shipment lifecycle events across:

- Postal operators
- Parcel carriers
- Express carriers
- Pickup point networks (PUDO)
- Locker networks
- Return logistics providers

The taxonomy acts as the single source of truth for:

- Tracking normalization
- Tracking validation
- Business workflows
- Reporting and analytics
- Notification triggering
- API responses

---

# Design Principles

## Canonical First

Carrier-specific statuses must always be mapped to a canonical status.

Example:

| Carrier   | Native Status       |
| --------- | ------------------- |
| DHL       | Shipment delivered  |
| UPS       | Delivered           |
| Colissimo | Livraison effectuée |

↓

```text
DELIVERED
```

---

## Immutable Core

Canonical statuses are maintained by the project and cannot be modified.

Users may extend the model using Business Statuses.

Example:

```text
IN_TRANSIT
  └─ AT_SORTING_CENTER
  └─ LINEHAUL
```

The core status remains unchanged.

---

## State Machine Driven

Statuses are not independent values.

Each status participates in a shipment lifecycle.

Transitions are validated using the canonical state machine.

---

# Status Categories

## PRE_SHIPMENT

Shipment information exists but transportation has not yet started.

### Statuses

```text
PENDING
INFO_RECEIVED
READY_FOR_PICKUP
```

---

## INBOUND

Carrier has physically taken possession of the shipment.

### Statuses

```text
PICKED_UP
```

---

## TRANSIT

Shipment is moving through the logistics network.

### Statuses

```text
IN_TRANSIT
ARRIVED_AT_FACILITY
DEPARTED_FACILITY
CUSTOMS_PROCESSING
```

---

## LAST_MILE

Shipment is approaching final delivery.

### Statuses

```text
OUT_FOR_DELIVERY

ARRIVED_AT_PICKUP_POINT
DELIVERED_TO_PICKUP_POINT

AVAILABLE_FOR_PICKUP
```

---

## DELIVERED

Successful completion of the delivery process.

### Statuses

```text
DELIVERED
PICKED_UP_BY_CUSTOMER
```

---

## DELIVERY_EXCEPTION

Delivery could not be completed as expected.

### Statuses

```text
DELIVERY_ATTEMPT_FAILED
ADDRESS_ISSUE
RECIPIENT_UNAVAILABLE
PICKUP_EXPIRED
```

---

## RETURN

Shipment is returning to sender.

### Statuses

```text
RETURN_INITIATED
RETURN_IN_TRANSIT
RETURN_DELIVERED
```

---

## EXCEPTION

Critical operational issues affecting shipment progress.

### Statuses

```text
EXCEPTION
LOST
DAMAGED
HELD
```

---

# Canonical Status Definitions

## PENDING

Shipment exists but carrier activity has not yet started.

---

## INFO_RECEIVED

Carrier has received shipment information.

---

## READY_FOR_PICKUP

Shipment is ready for carrier collection.

---

## PICKED_UP

Carrier has physically collected the shipment.

---

## IN_TRANSIT

Shipment is moving through the carrier network.

---

## ARRIVED_AT_FACILITY

Shipment has arrived at a logistics facility.

---

## DEPARTED_FACILITY

Shipment has left a logistics facility.

---

## CUSTOMS_PROCESSING

Shipment is undergoing customs clearance.

---

## OUT_FOR_DELIVERY

Shipment is assigned to a delivery route.

---

## ARRIVED_AT_PICKUP_POINT

Shipment has arrived at a pickup point or locker location.

The shipment is not necessarily available for customer retrieval yet.

---

## DELIVERED_TO_PICKUP_POINT

Shipment has been handed over to the pickup point or locker operator.

---

## AVAILABLE_FOR_PICKUP

Shipment is available for customer collection.

---

## DELIVERED

Shipment has been successfully delivered to the recipient.

---

## PICKED_UP_BY_CUSTOMER

Shipment has been successfully collected by the customer from a pickup point or locker.

---

## DELIVERY_ATTEMPT_FAILED

A delivery attempt was made but was unsuccessful.

---

## ADDRESS_ISSUE

Delivery failed because of an address problem.

---

## RECIPIENT_UNAVAILABLE

Delivery failed because the recipient was unavailable.

---

## PICKUP_EXPIRED

Shipment remained available for collection but was not retrieved within the allowed period.

---

## RETURN_INITIATED
