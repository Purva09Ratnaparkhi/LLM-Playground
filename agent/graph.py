from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import llm_node, should_continue


graph = StateGraph(AgentState)

graph.add_node("llm", llm_node)

graph.set_entry_point("llm")

graph.add_conditional_edges(
    "llm",
    should_continue,
    {
        "continue": "llm",
        "end": END,
    }
)

agent = graph.compile()
