import unittest
from modules.assessment_tracker import AssessmentTracker

class TestAssessmentTracker(unittest.TestCase):
    def test_record_and_evaluate(self):
        tracker = AssessmentTracker()
        tracker.record_result("u1", "q1", True)
        tracker.record_result("u1", "q2", False)
        result = tracker.evaluate_performance("u1")
        self.assertAlmostEqual(result["accuracy"], 0.5)