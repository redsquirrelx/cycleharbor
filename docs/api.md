# Application API

**Status:** Maintained

`AvailabilityService.list_available(station_id) -> list[str]`: available bike identifiers.

`RideActivationService.start(ride_id, rider_id, bike_id, when) -> Ride`: verifies fleet status, unlocks bicycle and persists a ride.

`RideCompletionService.finish(ride_id, when) -> Ride`: locks bicycle and saves completion time.

`FarePolicy.quote(ride) -> FareQuote`: independently interchangeable, fully priced quote for a completed ride.

`SettlementService.settle(ride_id) -> str`: captures a payable quote through the payment port and returns the receipt's external reference. No raw processor response is part of this API.

`RiderNotificationService.notify_receipt(rider_id, ride_id) -> None`: creates and sends a receipt message through the delivery port.

`MaintenanceTriage.report(bike_id, problem, when) -> RepairTicket`: accepts a field report and submits the ticket through the queue contract.

`RideWorkflow.run(ride_id, rider_id, bike_id, when) -> str`: performs a local rental lifecycle and returns the payment reference.
