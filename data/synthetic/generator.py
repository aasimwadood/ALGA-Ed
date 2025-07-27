
import json
import random
import os
from faker import Faker

fake = Faker()

DISABILITY_TYPES = ["ADHD", "dyslexia", "visual_impairment", "hearing_impairment"]


class SyntheticStudentGenerator:
    def __init__(self, count=10):
        self.count = count
        self.data = []

    def generate_profiles(self):
        for _ in range(self.count):
            profile = {
                "id": fake.uuid4(),
                "name": fake.name(),
                "age": random.randint(7, 18),
                "disability": random.choice(DISABILITY_TYPES),
                "engagement_pattern": [random.uniform(0.2, 0.9) for _ in range(5)],
                "task_completion_rate": round(random.uniform(0.4, 0.95), 2),
                "error_rate": round(random.uniform(0.05, 0.4), 2)
            }
            self.data.append(profile)

    def save_to_file(self, path="data/synthetic/synthetic_students.json"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.data, f, indent=4)


if __name__ == "__main__":
    generator = SyntheticStudentGenerator(count=50)
    generator.generate_profiles()
    generator.save_to_file()
    print("Synthetic data generated and saved.")
