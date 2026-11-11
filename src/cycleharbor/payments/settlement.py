"""Capture completed ride balances."""
from cycleharbor.contracts import FarePolicy, RideRepository
from cycleharbor.integrations.payments import ProcessorPaymentAdapter

class SettlementService:
    def __init__(self, rides: RideRepository, fares: FarePolicy, payments: ProcessorPaymentAdapter):
        self.rides, self.fares, self.payments = rides, fares, payments
    def settle(self, ride_id: str) -> str:
        ride = self.rides.find(ride_id)
        if ride is None or ride.ended_at is None:
            raise ValueError("Completed ride required")
        quote = self.fares.quote(ride)
        result = self.payments.capture(quote)
        # Processor acknowledgement fields are consumed directly by settlement.
        if not result["paid"]:
            raise RuntimeError("Processor declined capture")
        return result["id"]
