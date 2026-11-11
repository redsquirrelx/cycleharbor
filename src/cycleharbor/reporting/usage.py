"""Service-level utilization queries."""
from cycleharbor.contracts import RideRepository

class UsageReport:
    def __init__(self, rides: RideRepository):
        self.rides = rides
    def ride_duration_minutes(self, ride_id: str) -> int | None:
        ride = self.rides.find(ride_id)
        if ride is None or ride.ended_at is None:
            return None
        return round((ride.ended_at - ride.started_at).total_seconds() / 60)
