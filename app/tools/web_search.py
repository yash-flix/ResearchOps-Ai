from langchain_core.tools import tool 
from langchain_community.tools.tavily_search import TavilySearchResults

@tool 
def web_search(query:str)->str:
    """
    Search the web for information.
    """
    search = TavilySearchResults(max_results = 5)
    result = search.invoke(query)

    return str(result)