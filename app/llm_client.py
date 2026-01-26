import os
import httpx
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------- GEMINI SETUP ----------
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

GEMINI_MODEL = "models/gemini-2.5-flash"


async def call_gemini(messages, temperature=0.7):
    model = genai.GenerativeModel(GEMINI_MODEL)

    # Convert OpenAI-style messages → Gemini format
    prompt = "\n".join(
        f"{m['role'].upper()}: {m['content']}" for m in messages
    )

    response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature}
    )

    return response.text


# ---------- OLLAMA FALLBACK ----------
OLLAMA_URL = "http://localhost:11434/api/chat"


async def call_ollama(messages, model="mistral", temperature=0.7):
    payload = {
        "model": model,
        "messages": messages,
        "options": {"temperature": temperature},
        "stream": False,
    }

    timeout = httpx.Timeout(connect=30.0, read=300.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]


# ---------- UNIFIED INTERFACE ----------
async def call_llm(messages, model=None, temperature=0.7, max_tokens=256):
    # 1️⃣ Try Gemini first
    try:
        if GEMINI_API_KEY:
            text = await call_gemini(messages, temperature)
            return {
                "choices": [
                    {"message": {"content": text}}
                ]
            }
    except Exception as e:
        print("⚠️ Gemini failed, falling back to Ollama:", e)

    # 2️⃣ Fallback to Ollama
    text = await call_ollama(messages, temperature=temperature)
    return {
        "choices": [
            {"message": {"content": text}}
        ]
    }
