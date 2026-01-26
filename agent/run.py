import asyncio
from agent.graph import agent


async def run():
    initial_state = {
        "messages": [
            {
                "role": "system",
                "content":
                "You are an intelligent agent.\n"
                "If a calculation is required, use the calculator tool.\n\n"
                "Tool call format:\n"
                "TOOL: calculator\n"
                "INPUT: <expression>\n\n"
                "When you reach a final answer, respond with:\n"
                "FINAL ANSWER: <answer>"
            },   
            {"role": "user", "content": "What is 928374 * 182736?"},
        ]
    }

    final_state = await agent.ainvoke(initial_state)

    print(final_state["messages"][-1]["content"])


asyncio.run(run())
