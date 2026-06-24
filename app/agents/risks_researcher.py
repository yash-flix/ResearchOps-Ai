from app.llm.factory import get_fast_llm
from app.tools.web_search import web_search
from app.config.logger import logger

fast_llm = get_fast_llm()


def risks_researcher_node(state):

    context = state["raw_research_context"]

    summary = fast_llm.invoke(
        f"""
        Research task:
        {state['task']}

        Search Results:
        {context}

        Focus on:

        - Risks
        - Limitations
        - Failure modes
        - Regulatory concerns
        - Counterarguments
        """
    )
    logger.info("RISKS RESEARCHER EXECUTED")

    return {
        "research_results": [
            f"RISKS:\n{summary.content}"
        ]
    }