import unittest
from datetime import datetime, timezone, timedelta
from cycleharbor.domain.models import Bicycle
from cycleharbor.storage.memory import MemoryBicycleCatalog, MemoryRideRepository
from cycleharbor.integrations.locks import SimulatedLockGateway
from cycleharbor.rides.activation import RideActivationService
from cycleharbor.rides.completion import RideCompletionService
class RideTests(unittest.TestCase):
    def test_activation_and_completion(self):
        rides = MemoryRideRepository(); locks = SimulatedLockGateway()
        activation = RideActivationService(MemoryBicycleCatalog([Bicycle("b", "west")]), locks, rides)
        when = datetime(2026, 8, 1, tzinfo=timezone.utc)
        activation.start("r", "u", "b", when)
        finished = RideCompletionService(rides, locks).finish("r", when + timedelta(minutes=10))
        self.assertIsNotNone(finished.ended_at)
        self.assertNotIn("b", locks.unlocked)
