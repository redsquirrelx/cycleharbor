import unittest
from datetime import datetime, timezone
from cycleharbor.maintenance.triage import MaintenanceTriage
from cycleharbor.storage.memory import MemoryRepairQueue
class MaintenanceTests(unittest.TestCase):
    def test_report_creates_ticket(self):
        queue = MemoryRepairQueue()
        MaintenanceTriage(queue).report("b", "brake", datetime.now(timezone.utc))
        self.assertEqual(len(queue.tickets), 1)
