from typing import Literal

from app.graph.state import GraphState
from app.config import constants

MAX_RETRIES = 3


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
    if state.get("retry_count", 0) >= MAX_RETRIES:
        return "__end__"

    next_agent = state["next_agent"]

    if next_agent == "done":
        return "__end__"

    return next_agent