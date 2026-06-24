from app.tools.web_search import web_search
from app.config.constants import MAX_RESEARCH_CHARS

def research_collector_node(state):
    search_results = web_search.invoke(
        {"query" : state["task"]}
    )
    if isinstance(search_results, list):

        context = "\n\n".join(
            str(result)
            for result in search_results
        )

    else:
        context = str(search_results)
    return {
    "raw_research_context":
        context[:MAX_RESEARCH_CHARS]
}
