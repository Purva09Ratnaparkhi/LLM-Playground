from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest
from app.llm_client import call_llm

app = FastAPI(title="LLM Playground API")


@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": req.prompt},
        ]

        result = await call_llm(
            messages=messages,
            model=req.model,
            temperature=req.temperature,
            max_tokens=req.max_tokens,
        )

        reply = result["choices"][0]["message"]["content"]
        return {"reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
