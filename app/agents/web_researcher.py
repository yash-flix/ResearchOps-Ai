from langgraph.prebuilt import create_react_agent
from app.llm.factory import get_llm
from app.tools.web_search import web_search 

def build_web_search_agent():
    llm = get_llm()

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

def web_researcher_node(state) -> dict:
    agent = build_web_search_agent()

    result = agent.invoke({
        "messages":[
            {
                "role" : "user", 
                "content" : state["task"]
            }
        ]
    })

    findings = result["messages"][-1].content

    # Retry condition
    if not findings:
        return {
            "retry_count": state["retry_count"] + 1
        }

    return {
        "research_results" : findings ,
         "next_agent": "supervisor"
    }

