from langchain_core.tools import tool
from langchain_tavily import TavilySearch

search = TavilySearch(max_results=5)

@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    results = search.invoke(query)
    return str(results)