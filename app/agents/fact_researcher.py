from app.llm.factory import get_llm
from app.tools.web_search import web_search

llm = get_llm()


def facts_researcher_node(state):
    """
    Researches factual information about the task.
    """

    # Retrieve information from the web
    search_results = web_search.invoke(
        {"query": state["task"]}
    )

    #  Convert results into a clean context string
    if isinstance(search_results, list):

        context = "\n\n".join(
            str(result)
            for result in search_results
        )

    else:
        context = str(search_results)

   
    summary = llm.invoke(
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


    return {
        "research_results": [
            f"FACTS RESEARCH\n\n{summary.content}"
        ]
    }