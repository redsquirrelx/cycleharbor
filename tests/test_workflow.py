import unittest
from datetime import datetime, timezone
from cycleharbor.bootstrap import build_local_app
class WorkflowTests(unittest.TestCase):
    def test_local_workflow_returns_processor_reference(self):
        workflow, _ = build_local_app()
        self.assertEqual(workflow.run("r1", "u1", "bk-100", datetime.now(timezone.utc)), "processor-001")
