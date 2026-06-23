from typing import Literal 
from app.graph.state import GraphState

def supervisor_router(
    state: GraphState
) -> Literal[
    "web_researcher",
    "analyst",
    "writer",
    "reviewer",
    "evaluator",
    "__end__"
]:
    next_agent = state["next_agent"]

    if next_agent == "done":
        return "__end__"
    
    return next_agent
            