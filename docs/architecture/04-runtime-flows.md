# CH-104 — Runtime flows

**Status:** Approved

## Start ride

`RideWorkflow` calls `RideActivationService.start`, which checks `BicycleCatalog`, invokes `LockGateway.unlock`, and persists the ride through `RideRepository.save`. The service receives a normalized boolean acknowledgement regardless of controller hardware.

## Finish ride and charge

`RideCompletionService.finish` locks the bicycle and persists the completed ride. `SettlementService.settle` requests a `FareQuote` from a selected `FarePolicy`, passes the quote to `PaymentGateway.capture`, and reads `PaymentReceipt.accepted` and `PaymentReceipt.external_reference`. Device, processor and transport metadata never participate in settlement decisions.

## Issue notification

After successful settlement the workflow calls `RiderNotificationService`, which delegates delivery of a prepared `RiderMessage` to `MessageGateway`.

## Repair request

`MaintenanceTriage.report` builds a `RepairTicket` and submits it via `RepairQueue.enqueue`. Backlog ownership remains within the queue adapter, not the service.
