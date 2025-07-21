# Streamlit UI, GPT/DALL·E/Whisper integration, RL, scoring, datasets, SQLite persistence

import os
import openai
import json
import random
import numpy as np
import pandas as pd
import streamlit as st
import sqlite3

# ------------------- Configuration -------------------
openai.api_key = os.getenv("OPENAI_API_KEY")
DB_PATH = "algaed_users.db"

# ---------------- Database Setup ----------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    profile TEXT,
                    progress TEXT
                )''')
    conn.commit()
    conn.close()

def save_user_progress(username, topic, score):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT progress FROM users WHERE username=?", (username,))
    row = c.fetchone()
    progress = json.loads(row[0]) if row and row[0] else {}
    progress[topic] = score
    c.execute("UPDATE users SET progress=? WHERE username=?", (json.dumps(progress), username))
    conn.commit()
    conn.close()

def get_user_profile(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT profile FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row and row[0] else user_profile_example()

def get_user_progress(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT progress FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row and row[0] else {}

def save_user_profile(username, profile):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO users (username, profile, progress) VALUES (?, ?, ?)",
              (username, json.dumps(profile), json.dumps({})))
    conn.commit()
    conn.close()

def load_all_users():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT username, profile, progress FROM users", conn)
    conn.close()
    return df

# ---------------- GPT Modules ----------------
def generate_simplified_text(prompt, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an educational assistant simplifying content for students with disabilities."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

def generate_quiz(topic):
    prompt = f"Create a short 3-question multiple choice quiz on {topic} with answer key."
    return generate_simplified_text(prompt)

# ---------------- DALL·E & Whisper ----------------
def generate_visual(description):
    response = openai.Image.create(prompt=description, n=1, size="512x512")
    return response['data'][0]['url']

def generate_audio(text, lang="en"):
    from gtts import gTTS
    audio = gTTS(text=text, lang=lang)
    audio.save("output.mp3")
    return "output.mp3"

# ---------------- User Profile Simulation ----------------
def user_profile_example():
    return {
        "user_id": "student123",
        "cognitive_level": "medium",
        "visual_impairment": False,
        "auditory_impairment": True,
        "preferred_modality": "visual",
        "attention_span": "short",
        "learning_challenges": ["ADHD"]
    }

def adapt_content(profile, content, topic=None, progress=None):
    if profile.get("attention_span") == "short" or (progress and progress.get(topic, 0) < 0.5):
        content = generate_simplified_text("Summarize in 3 bullet points: " + content)
    if profile.get("auditory_impairment"):
        content += "\n[Captions enabled. Avoid audio-only instructions.]"
    return content

# ---------------- RL Engine ----------------
class SimpleRLAgent:
    def __init__(self, actions):
        self.q_table = {a: 0 for a in actions}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.2

    def select_action(self):
        if random.random() < self.exploration_rate:
            return random.choice(list(self.q_table.keys()))
        return max(self.q_table, key=self.q_table.get)

    def update(self, action, reward):
        q = self.q_table[action]
        self.q_table[action] = q + self.learning_rate * (reward + self.discount_factor * max(self.q_table.values()) - q)

ACTIONS = ["simplify_text", "add_visual", "add_audio", "repeat_with_hints"]
rl_agent = SimpleRLAgent(ACTIONS)

def simulate_engagement(action):
    return random.uniform(0.4, 1.0)

# ---------------- Quiz Scoring ----------------
def score_quiz(user_answers, correct_answers):
    correct = sum(u.strip().lower() == c.strip().lower() for u, c in zip(user_answers, correct_answers))
    return correct / len(correct_answers)

# ---------------- Dataset Loader ----------------
def load_dataset(name):
    path = f"data/{name}.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df.head(10)
    else:
        return pd.DataFrame()

# ---------------- Streamlit UI ----------------
def main():
    init_db()
    st.set_page_config(page_title="ALGA-Ed Demo", layout="wide")
    st.title("📚 ALGA-Ed: Adaptive Learning for Disabilities")

    with st.sidebar:
        st.header("👤 User Login")
        username = st.text_input("Username", value="student123")
        if st.button("Create/Update User"):
            profile = user_profile_example()
            save_user_profile(username, profile)
            st.success("User profile saved.")

        if st.checkbox("📊 Admin Dashboard"):
            st.subheader("All Users (Admin View)")
            st.dataframe(load_all_users())

    topic = st.text_input("Enter a topic to learn", value="photosynthesis")
    user_profile = get_user_profile(username)
    user_progress = get_user_progress(username)

    if st.button("Generate Personalized Content"):
        with st.spinner("Generating..."):
            adapted = adapt_content(user_profile, topic, topic, user_progress)
            st.subheader("📘 Adapted Content")
            st.write(adapted)
            image_url = generate_visual(f"diagram for {topic}")
            st.image(image_url, caption="Visual Aid")
            audio_path = generate_audio(adapted)
            st.audio(audio_path)

    if st.button("Generate Quiz"):
        st.subheader("📝 Quiz")
        quiz = generate_quiz(topic)
        st.text_area("Quiz", quiz, height=200)
        user_answers = st.text_input("Enter your answers (comma-separated)")
        correct_answers = ["a", "b", "c"]  # placeholder
        if st.button("Submit Quiz"):
            score = score_quiz(user_answers.split(","), correct_answers)
            save_user_progress(username, topic, score)
            st.success(f"Quiz Score: {score*100:.1f}% saved.")

    if st.button("Run RL Feedback Loop"):
        action = rl_agent.select_action()
        reward = simulate_engagement(action)
        rl_agent.update(action, reward)
        st.success(f"Selected Action: {action}, Reward: {reward:.2f}")

    st.subheader("📂 Dataset Preview")
    dataset_name = st.selectbox("Choose dataset", ["ednet_sample", "assistments_sample"])
    df = load_dataset(dataset_name)
    st.dataframe(df)

if __name__ == "__main__":
    main()
