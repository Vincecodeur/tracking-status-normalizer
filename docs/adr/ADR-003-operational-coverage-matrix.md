# ADR-003: Operational Coverage Matrix

## Status

Accepted

## Date

2026-07-09

## Context

A governance model requires a way to determine what logistics flows are represented by a carrier catalog.

## Decision

An Operational Coverage Matrix is introduced.

It evaluates what logistics capabilities are represented by the catalog.

## Coverage Levels

FULL

All required statuses are present.

PARTIAL

Some required statuses are present.

NONE

No required statuses are present.

## Capabilities

DIRECT_DELIVERY

Required statuses:

- IN_TRANSIT
- OUT_FOR_DELIVERY
- DELIVERED

PUDO

Required statuses:

- ARRIVED_AT_PICKUP_POINT
- AVAILABLE_FOR_PICKUP
- PICKUP_EXPIRED

LOCKER

Required statuses:

- DELIVERED_TO_PICKUP_POINT
- AVAILABLE_FOR_PICKUP
- PICKED_UP_BY_CUSTOMER

OUT_OF_HOME_DELIVERY

Derived capability:

- PUDO OR LOCKER

RETURNS

Required statuses:

- RETURN_INITIATED
- RETURN_IN_TRANSIT
- RETURN_DELIVERED

CUSTOMS

Required statuses:

- CUSTOMS_PROCESSING

EXCEPTION_MANAGEMENT

Required statuses:

- EXCEPTION
- LOST
- DAMAGED
- HELD

## Consequences

The Operational Coverage Matrix becomes the foundation for:

- Readiness Assessment
- Gap Analysis
- Recommendations
- Maturity Score
