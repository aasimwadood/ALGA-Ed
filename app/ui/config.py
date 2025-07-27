
# -----------------------------
# File: app/config.py
# -----------------------------

import os

# Environment variable keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # Can be set in .env or deployment config

# Paths for datasets and generated content
DATA_DIR = "data/"
AUDIO_OUTPUT_DIR = os.path.join(DATA_DIR, "audio/")
IMAGE_OUTPUT_DIR = os.path.join(DATA_DIR, "images/")
PROFILE_SAVE_PATH = os.path.join(DATA_DIR, "profiles/")
