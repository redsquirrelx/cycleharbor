# ADR-0001 — Stable hardware lock port

**Status:** Accepted

## Context

Physical dock stations and local simulators expose different command semantics.

## Decision

Services depend on `LockGateway.unlock/lock`, returning booleans. Device response payloads are normalized inside each adapter; no station-port identifier or controller acknowledgement dictionary is exposed to ride services.

## Consequences

A simulator or station device driver can be substituted without changing the ride activation and completion code.
