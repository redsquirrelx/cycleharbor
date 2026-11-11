import unittest
from cycleharbor.notifications.gateways import MemoryMessageGateway
from cycleharbor.notifications.service import RiderNotificationService
class NotificationTests(unittest.TestCase):
    def test_receipt_notice(self):
        gateway = MemoryMessageGateway()
        RiderNotificationService(gateway).notify_receipt("rider", "ride")
        self.assertEqual(gateway.sent[0].template, "ride-receipt")
