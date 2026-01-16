from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str
    model: str = "mistralai/mistral-7b-instruct"
    temperature: float = 0.7
    max_tokens: int = 256
