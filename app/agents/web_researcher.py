from langgraph.prebuilt import create_react_agent
from app.llm.factory import get_llm
from app.tools.web_search import web_search 
from langsmith import traceable

llm = get_llm()


def build_web_search_agent():
   
    return create_react_agent(
        model = llm, 
        tools=[web_search],
        prompt="""
        You are an expert research agent.

        Your responsibilities:

        - Search for accurate information
        - Verify claims
        - Gather useful facts
        - Return detailed findings

        Always use web_search when information
        is required.
        """
    )



@traceable(name="web_researcher")
def web_researcher_node(state):
    raw_results = web_search.invoke(
        {"query": state["task"]}
    )
    summary = llm.invoke(
    f"""
    Summarize these search results.

    Results:
    {raw_results}
    """
)
    tokens = (
    summary
    .response_metadata
    .get("token_usage", {})
    .get("total_tokens", 0)
)

    return {
    "research_results": summary.content ,
    "token_usage": {
        **state["token_usage"],
        "web_researcher": tokens
    },
     "next_agent": "supervisor"
}