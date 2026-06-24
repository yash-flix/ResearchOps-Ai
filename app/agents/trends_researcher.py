from app.llm.factory import get_llm
from app.tools.web_search import web_search

llm = get_llm()


def trends_researcher_node(state):

    search_results = web_search.invoke(
        {"query": state["task"]}
    )

    if isinstance(search_results, list):

        context = "\n\n".join(
            str(result)
            for result in search_results
        )

    else:
        context = str(search_results)

    summary = llm.invoke(
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

    return {
        "research_results": [
            f"TRENDS:\n{summary.content}"
        ]
    }