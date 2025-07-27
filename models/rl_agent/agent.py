# -----------------------------
# File: models/rl_agent/agent.py
# -----------------------------

import random
from typing import Dict

class RLContentAdapter:
    def __init__(self):
        self.state = None

    def choose_action(self, performance: float) -> str:
        if performance < 0.4:
            return "simplify"
        elif 0.4 <= performance <= 0.75:
            return "maintain"
        else:
            return "advance"

    def update_state(self, feedback: Dict[str, float]):
        # Placeholder for Q-learning or bandit policy
        self.state = feedback
