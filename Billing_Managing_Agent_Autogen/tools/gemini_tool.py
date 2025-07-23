import os
from autogen import GeminiAPIWrapper

def get_gemini_config():
    return [{
        "api_key": os.environ.get("GEMINI_API_KEY"),
        "api_type": "google_gemini"
    }]
