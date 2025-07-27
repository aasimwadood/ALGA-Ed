# -----------------------------
# File: modules/user_profile.py
# -----------------------------

import json
import datetime
from typing import Dict, List, Any

class UserProfile:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.profile_data = {
            "cognitive": {},
            "sensory": {},
            "behavioral": {},
            "preferences": {},
            "last_updated": str(datetime.datetime.utcnow())
        }

    def update_profile(self, key: str, data: Dict[str, Any]):
        if key in self.profile_data:
            self.profile_data[key].update(data)
        self.profile_data["last_updated"] = str(datetime.datetime.utcnow())

    def get_profile(self) -> Dict[str, Any]:
        return self.profile_data

    def save_to_file(self, path="data/profiles/"):
        with open(f"{path}{self.user_id}.json", "w") as f:
            json.dump(self.profile_data, f, indent=4)

