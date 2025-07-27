
import unittest
from modules.adaptive_feedback import AdaptiveFeedbackSystem

class TestAdaptiveFeedbackSystem(unittest.TestCase):
    def test_feedback_action(self):
        system = AdaptiveFeedbackSystem()
        action = system.get_feedback_action({"accuracy": 0.9})
        self.assertEqual(action, "advance")
