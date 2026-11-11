import unittest
from cycleharbor.domain.models import FareQuote
from cycleharbor.integrations.payments import SandboxPaymentGateway
from cycleharbor.integrations.locks import SimulatedLockGateway, StationLockAdapter, DockController
class ContractTests(unittest.TestCase):
    def test_sandbox_capture_returns_domain_receipt(self):
        receipt = SandboxPaymentGateway().capture(FareQuote("r", 500))
        self.assertTrue(receipt.accepted)
    def test_lock_adapters_return_boolean(self):
        self.assertTrue(SimulatedLockGateway().unlock("b"))
        self.assertTrue(StationLockAdapter(DockController(), {"b":"dock-1"}).unlock("b"))
