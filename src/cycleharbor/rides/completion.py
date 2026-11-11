"""Ride completion and final lock verification."""
from dataclasses import replace
from datetime import datetime
from cycleharbor.contracts import LockGateway, RideRepository

class RideCompletionService:
    def __init__(self, rides: RideRepository, locks: LockGateway):
        self.rides, self.locks = rides, locks
    def finish(self, ride_id: str, when: datetime):
        ride = self.rides.find(ride_id)
        if ride is None:
            raise KeyError(ride_id)
        if not self.locks.lock(ride.bike_id):
            raise RuntimeError("Unable to close dock")
        completed = replace(ride, ended_at=when)
        self.rides.save(completed)
        return completed
