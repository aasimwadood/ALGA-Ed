# -----------------------------
# File: models/audio_gen/whisper_gen.py
# -----------------------------

from gtts import gTTS
import tempfile

def generate_audio(text: str, lang: str = 'en') -> str:
    tts = gTTS(text, lang=lang)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

