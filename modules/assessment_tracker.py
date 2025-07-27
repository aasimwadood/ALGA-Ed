

# -----------------------------
# File: modules/assessment_tracker.py
# -----------------------------

from typing import List, Dict
import random

class AssessmentTracker:
    def __init__(self):
        self.records = {}

    def record_result(self, user_id: str, question_id: str, correct: bool):
        self.records.setdefault(user_id, []).append({
            "question_id": question_id,
            "correct": correct
        })

    def evaluate_performance(self, user_id: str) -> Dict[str, float]:
        user_data = self.records.get(user_id, [])
        if not user_data:
            return {"accuracy": 0.0}
        correct_answers = sum(1 for record in user_data if record["correct"])
        return {"accuracy": correct_answers / len(user_data)}

    def generate_quiz(self, topic: str, difficulty: str = "medium") -> List[Dict[str, str]]:
        sample_questions = [
            {"question": f"What is the definition of {topic}?", "answer": "Sample answer."},
            {"question": f"Explain the concept of {topic} with an example.", "answer": "Sample explanation."}
        ]
        return random.sample(sample_questions, k=min(2, len(sample_questions)))
