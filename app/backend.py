
# -----------------------------
# File: app/backend.py
# -----------------------------

from modules.user_profile import UserProfile
from modules.adaptive_feedback import AdaptiveFeedbackSystem
from modules.assessment_tracker import AssessmentTracker
from modules.accessibility import apply_accessibility_settings
from models.text_gen.gpt_gen import generate_simplified_text
from models.image_gen.dalle_gen import generate_educational_image
from models.audio_gen.whisper_gen import generate_audio

feedback_system = AdaptiveFeedbackSystem()
tracker = AssessmentTracker()


def run_learning_session(user_id: str, topic: str, user_profile_data: dict):
    profile = UserProfile(user_id)
    profile.update_profile("preferences", user_profile_data.get("preferences", {}))
    quiz = tracker.generate_quiz(topic)
    
    simplified_content = generate_simplified_text(f"Explain {topic} simply.")
    visual_url = generate_educational_image(f"Diagram for {topic}")
    audio_path = generate_audio(simplified_content)

    accessible_content = apply_accessibility_settings(simplified_content, profile.get_profile())
    
    return {
        "text": accessible_content,
        "image": visual_url,
        "audio": audio_path,
        "quiz": quiz
    }