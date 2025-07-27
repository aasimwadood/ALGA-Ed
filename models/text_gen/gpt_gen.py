# -----------------------------
# File: models/text_gen/gpt_gen.py
# -----------------------------

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_simplified_text(prompt: str, level: str = "simple") -> str:
    system_instruction = f"Simplify educational content to a {level} level for accessibility."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
