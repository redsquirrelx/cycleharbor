# ADR-0003 — Fare policy substitution

**Status:** Accepted

## Context

Flat, metered and promotional products share the same checkout pipeline.

## Decision

`FarePolicy.quote` always calculates a complete nonnegative payable amount. Promotions are independently executable fare policies and not partial discounts requiring an external price base.

## Consequences

Checkout and settlement remain agnostic to policy class and pricing campaign details.
