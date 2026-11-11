# CH-101 — System context

**Status:** Approved · **Scope:** station-based short-distance bicycle rentals.

The city operations team owns the bicycle inventory, fixed stations and repair work orders. Riders interact with bicycle locks and the ride application. CycleHarbor records the lifecycle of each ride, quotes a final amount, captures a payment and issues a receipt notification.

The external dependencies are dock controllers, payment processors and messaging transports. These systems provide device commands, financial capture and message delivery; they do not own fare policy, trip completion or maintenance decision-making.

## Business capabilities

- Fleet discovery across stations, with out-of-service bicycles excluded.
- Ride activation and completion under stable application contracts.
- Fare quotation and payment capture without payment-vendor semantics in business services.
- Rider communication through a delivery port.
- Repair intake through an asynchronous work queue.

The local deployment uses in-memory state for rentals and a simulator for locks, but the ports remain identical across deployment profiles.
