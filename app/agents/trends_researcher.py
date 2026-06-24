from app.llm.factory import get_fast_llm
from app.tools.web_search import web_search
from app.config.logger import logger

fast_llm = get_fast_llm()


def trends_researcher_node(state):

    context = state["raw_research_context"]


    summary = fast_llm.invoke(
        f"""
        Research task:
        {state['task']}

        Search Results:
        {context}

        Focus on:

        - Emerging trends
        - Future developments
        - Industry direction
        - Long term implications
        """
    )
    logger.info("TRENDS RESEARCHER EXECUTED")

    return {
        "research_results": [
            f"TRENDS:\n{summary.content}"
        ]
    }