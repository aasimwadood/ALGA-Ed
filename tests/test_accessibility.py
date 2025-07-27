import unittest
from modules.accessibility import apply_accessibility_settings

class TestAccessibility(unittest.TestCase):
    def test_high_contrast_and_large_text(self):
        content = "Welcome"
        profile = {"preferences": {"high_contrast": True, "large_text": True}}
        modified = apply_accessibility_settings(content, profile)
        self.assertIn("background:black", modified)
        self.assertIn("font-size:1.5em", modified)