import unittest
from datetime import datetime, timezone, timedelta
from cycleharbor.domain.models import Ride
from cycleharbor.pricing.policies import FlatFarePolicy, MinuteFarePolicy
class PricingTests(unittest.TestCase):
    def test_flat_fare(self):
        ride = Ride("r", "u", "b", datetime.now(timezone.utc))
        self.assertEqual(FlatFarePolicy(350).quote(ride).amount_cents, 350)
    def test_minute_fare(self):
        start = datetime.now(timezone.utc)
        ride = Ride("r", "u", "b", start, start + timedelta(minutes=10))
        self.assertEqual(MinuteFarePolicy().quote(ride).amount_cents, 300)
