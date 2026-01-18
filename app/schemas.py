from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    prompt: str
    model: str = "mistralai/devstral-2512:free"
    temperature: float = 0.7
    max_tokens: int = 256
