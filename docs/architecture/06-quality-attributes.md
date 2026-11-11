# CH-106 — Quality attributes

**Status:** Approved

## Abstraction and evolvability

Changing a payment provider, dock lock controller or repair queue implementation should require a new adapter and a composition change only, not updates to application services. Abstract ports must hide device and provider-specific formats. Port implementations must satisfy the same behavior and return types, not merely expose methods with matching names.

## Functional consistency

A fare policy is replaceable wherever `FarePolicy` is expected. A complete quote always has a nonnegative amount, and consumers do not branch on the selected policy implementation.

## Testability

Local tests exercise core services using memory adapters or contract-compatible fakes. Contract verification for infrastructure adapters checks both data shape and domain-level semantics.

## Operability

Services report failures through domain exceptions and values, not raw HTTP or remote device status objects.
