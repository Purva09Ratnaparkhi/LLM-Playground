import httpx
from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL


async def call_llm(messages, model, temperature, max_tokens):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            OPENROUTER_BASE_URL,
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        return response.json()
