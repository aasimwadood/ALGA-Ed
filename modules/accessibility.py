
# -----------------------------
# File: modules/accessibility.py
# -----------------------------

def apply_accessibility_settings(content: str, profile: Dict[str, any]) -> str:
    settings = profile.get("preferences", {})
    if settings.get("high_contrast"):
        content = f"<div style='color:white; background:black'>{content}</div>"
    if settings.get("large_text"):
        content = f"<div style='font-size:1.5em'>{content}</div>"
    return content

