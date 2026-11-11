# ADR-0005 — Centralized composition

**Status:** Accepted

## Context

Integration selection should not be scattered across domain workflows.

## Decision

The composition root, `bootstrap.py`, constructs concrete lock, payment, messaging and maintenance adapters. Services accept only their contracts via injection.

## Consequences

Adapters can be replaced in one place and services can be unit-tested with contract-compatible fakes.
