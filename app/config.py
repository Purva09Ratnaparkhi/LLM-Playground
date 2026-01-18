import os
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

print("OPENROUTER_API_KEY loaded:", OPENROUTER_API_KEY is not None)

if not OPENROUTER_API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY")
