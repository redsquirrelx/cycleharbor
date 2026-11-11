"""Command line walkthrough."""
import argparse
from datetime import datetime, timezone
from cycleharbor.bootstrap import build_local_app

def main():
    parser = argparse.ArgumentParser(description="CycleHarbor operations")
    parser.add_argument("command", nargs="?", default="demo", choices=["demo"])
    parser.parse_args()
    workflow, _ = build_local_app()
    receipt = workflow.run("ride-001", "rider-001", "bk-100", datetime.now(timezone.utc))
    print(f"Ride completed; receipt: {receipt}")
