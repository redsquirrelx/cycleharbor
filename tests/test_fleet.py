import unittest
from cycleharbor.domain.models import Bicycle
from cycleharbor.storage.memory import MemoryBicycleCatalog
from cycleharbor.fleet.availability import AvailabilityService
class FleetTests(unittest.TestCase):
    def test_only_operational_bikes_are_available(self):
        catalog = MemoryBicycleCatalog([Bicycle("a", "west"), Bicycle("b", "west", False)])
        self.assertEqual(AvailabilityService(catalog).list_available("west"), ["a"])
