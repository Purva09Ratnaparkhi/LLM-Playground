from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest
from app.llm_client import call_llm
from app.memory import get_memory, add_message, trim_memory
import httpx

app = FastAPI(title="LLM Playground API")

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # 1) Fetch or initialize memory for this session
        messages = get_memory(req.session_id)
        messages = trim_memory(messages)

        # 2) Add user's message to memory
        add_message(req.session_id, "user", req.prompt)

        # 3) Call the LLM with full conversation history
        result = await call_llm(
            messages=messages,
            model=req.model,
            temperature=req.temperature,
            max_tokens=req.max_tokens,
        )

        # 4) Extract assistant reply
        reply = result["choices"][0]["message"]["content"]

        # 5) Add assistant reply to memory
        add_message(req.session_id, "assistant", reply)

        # 6) Return response
        return {"reply": reply}


    except httpx.HTTPStatusError:
        raise HTTPException(
                status_code=502,
                detail="LLM provider error. Please try again."
            )
        
    except Exception:
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )

