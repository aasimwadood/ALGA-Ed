# -----------------------------
# File: modules/adaptive_feedback.py
# -----------------------------

from typing import Dict
from models.rl_agent.agent import RLContentAdapter

class AdaptiveFeedbackSystem:
    def __init__(self):
        self.agent = RLContentAdapter()

    def get_feedback_action(self, performance_metrics: Dict[str, float]) -> str:
        avg_score = sum(performance_metrics.values()) / len(performance_metrics)
        return self.agent.choose_action(avg_score)

    def update_policy(self, feedback: Dict[str, float]):
        self.agent.update_state(feedback)