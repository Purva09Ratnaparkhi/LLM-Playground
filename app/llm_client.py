import asyncio
import httpx
from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL


async def call_llm(messages, model, temperature, max_tokens, retries=3):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "LLM Playground API",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    for attempt in range(retries):
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(
                    OPENROUTER_BASE_URL,
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
                return response.json()

        except Exception as e:
            if attempt == retries - 1:
                raise e
            await asyncio.sleep(2 ** attempt)
