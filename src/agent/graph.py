from langgraph.graph import StateGraph, END
from src.agent.state import AgentState
from src.agent.nodes import cybersecurity_node, summary_node, block_node

# 1. Initialize the state graph with our schema
workflow = StateGraph(AgentState)

# 2. Register the nodes
workflow.add_node("cybersecurity", cybersecurity_node)
workflow.add_node("summary", summary_node)
workflow.add_node("block", block_node)

# 3. Set the pipeline entrypoint
workflow.set_entry_point("cybersecurity")

# 4. Define conditional routing logic
def router_edge(state: AgentState) -> str:
    """
    Inspects the security status and routes the state to the correct node.
    """
    if state["security_status"] == "compromised":
        return "block"
    return "summary"

# 5. Connect the nodes with conditional routing rules
workflow.add_conditional_edges(
    "cybersecurity",
    router_edge,
    {
        "block": "block",
        "summary": "summary"
    }
)

# 6. Set terminal connections
workflow.add_edge("summary", END)
workflow.add_edge("block", END)

compiled_graph = workflow.compile()