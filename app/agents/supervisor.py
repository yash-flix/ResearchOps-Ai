from app.graph.state import GraphState
from app.config.logger import logger
from langsmith import traceable


@traceable(name="supervisor")
def supervisor_node(state: GraphState):

    if not state.get("raw_research_context"):
        next_agent = "research_collector"

    elif not state.get("research_results"):
        next_agent = "planner"

    elif not state.get("analysis_results"):
        next_agent = "analyst"

    elif not state.get("report"):
        next_agent = "writer"

    elif not state.get("approved"):
        next_agent = "reviewer"

    elif not state.get("evaluation_results"):
        next_agent = "evaluator"

    else:
        next_agent = "done"

    if state["review_iterations"] >= 3:
        next_agent = "evaluator"

    logger.info(
        f"""
======== SUPERVISOR ========

Next Agent:
{next_agent}

Research Results:
{len(state.get("research_results", []))}

Raw Research Available:
{bool(state.get("raw_research_context"))}

Analysis Exists:
{bool(state.get("analysis_results"))}

Report Exists:
{bool(state.get("report"))}

Approved:
{state.get("approved")}

Evaluation Exists:
{bool(state.get("evaluation_results"))}

============================
"""
    )

    return {
        "next_agent": next_agent
    }