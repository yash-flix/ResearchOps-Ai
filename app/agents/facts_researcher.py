from app.llm.factory import get_fast_llm
from app.tools.web_search import web_search
from app.config.logger import logger

fast_llm = get_fast_llm()


def facts_researcher_node(state):
    """
    Researches factual information about the task.
    """

    # Retrieve information from the web
    context = state["raw_research_context"]

   
    summary = fast_llm.invoke(
        f"""
        You are a factual research analyst.

        Research Task:
        {state["task"]}

        Search Results:
        {context}

        Instructions:
        - Extract only verified facts.
        - Include important statistics and numbers.
        - Include evidence and findings.
        - Ignore opinions unless supported by evidence.
        - Be concise and structured.

        Output Format:

        Key Facts:
        - ...

        Statistics:
        - ...

        Evidence:
        - ...

        Verified Findings:
        - ...
        """
    )

    logger.info("FACTS RESEARCHER EXECUTED")
    return {
        "research_results": [
            f"FACTS RESEARCH\n\n{summary.content}"
        ]
    }