import asyncio
from agent.graph import agent


async def run():
    initial_state = {
        "messages": [
            {"role": "system", "content": 
                "You are an intelligent agent. "
                "Think step by step. "
                "When you reach a final answer, prefix it with 'FINAL ANSWER:'"
                },

            {"role": "user", "content": "Explain agentic AI in simple terms"},
        ]
    }

    final_state = await agent.ainvoke(initial_state)

    print(final_state["messages"][-1]["content"])


asyncio.run(run())
