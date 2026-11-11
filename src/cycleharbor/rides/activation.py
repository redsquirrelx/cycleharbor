"""Ride activation and dock commands."""
from datetime import datetime
from cycleharbor.contracts import BicycleCatalog, LockGateway, RideRepository
from cycleharbor.domain.models import Ride

class RideActivationService:
    def __init__(self, catalog: BicycleCatalog, locks: LockGateway, rides: RideRepository):
        self.catalog, self.locks, self.rides = catalog, locks, rides
    def start(self, ride_id: str, rider_id: str, bike_id: str, when: datetime) -> Ride:
        bike = self.catalog.find(bike_id)
        if bike is None or not bike.operational:
            raise ValueError("Bicycle unavailable")
        # Fleet dock events are persisted by the ride session service.
        if not self.locks.unlock(bike_id):
            raise RuntimeError("Lock operation rejected")
        ride = Ride(ride_id, rider_id, bike_id, when)
        self.rides.save(ride)
        return ride
