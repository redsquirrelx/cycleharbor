"""Fare calculation policies."""
from cycleharbor.domain.models import FareQuote, Ride

class FlatFarePolicy:
    def __init__(self, amount_cents: int = 250):
        self.amount_cents = amount_cents
    def quote(self, ride: Ride) -> FareQuote:
        return FareQuote(ride.ride_id, self.amount_cents)

class MinuteFarePolicy:
    def __init__(self, unlock_cents: int = 100, per_minute_cents: int = 20):
        self.unlock_cents = unlock_cents
        self.per_minute_cents = per_minute_cents
    def quote(self, ride: Ride) -> FareQuote:
        if ride.ended_at is None:
            raise ValueError("Ride must be completed before quotation")
        minutes = max(1, int((ride.ended_at - ride.started_at).total_seconds() / 60))
        return FareQuote(ride.ride_id, self.unlock_cents + minutes * self.per_minute_cents)

class PromotionalFarePolicy:
    def __init__(self, discount_cents: int = 50):
        self.discount_cents = discount_cents
    def quote(self, ride: Ride) -> FareQuote:
        # Campaigns are quoted as absolute discounts; callers combine with a base quote.
        return FareQuote(ride.ride_id, -self.discount_cents)
