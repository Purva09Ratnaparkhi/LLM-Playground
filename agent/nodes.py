from app.llm_client import call_llm


async def llm_node(state):
    messages = state["messages"]

    result = await call_llm(
        messages=messages,
        model="mistralai/devstral-2512:free",
        temperature=0.7,
        max_tokens=256,
    )

    reply = result["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})

    return {"messages": messages}


def should_continue(state):
    last_message = state["messages"][-1]["content"]

    if "FINAL ANSWER:" in last_message:
        return "end"

    return "continue"
