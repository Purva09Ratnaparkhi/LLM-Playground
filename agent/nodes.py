from app.llm_client import call_llm
from agent.tools import calculator

async def llm_node(state):
    messages = state["messages"]

    result = await call_llm(
        messages=messages,
        temperature=0.7,
        max_tokens=256,
    )

    reply = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    # TOOL EXECUTION
    if reply.startswith("TOOL:"):
        print("🛠️ TOOL INVOCATION DETECTED")

        tool_name = reply.splitlines()[0].replace("TOOL:", "").strip()
        tool_input = reply.splitlines()[1].replace("INPUT:", "").strip()

        print(f"🧰 Tool name: {tool_name}")
        print(f"📥 Tool input: {tool_input}")

        if tool_name == "calculator":
            observation = calculator(tool_input)

            print(f"📤 Tool output: {observation}")

            messages.append(
                {"role": "system", "content": f"OBSERVATION: {observation}"}
            )
    else:
        print("🤖 LLM answered without using any tool")


    return {"messages": messages}


def should_continue(state):
    last_message = state["messages"][-1]["content"]

    if "FINAL ANSWER:" in last_message:
        return "end"

    return "continue"
