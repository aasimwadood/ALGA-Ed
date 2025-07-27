# -----------------------------
# File: models/image_gen/dalle_gen.py
# -----------------------------

import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_educational_image(prompt: str, size: str = "512x512") -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )
    return response["data"][0]["url"]

