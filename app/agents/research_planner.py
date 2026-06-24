from langgraph.constants import Send 

def planner_node(state):
    return [
        Send(
            "facts_researcher" ,
            {
            **state , 
            "research_type" : "facts"
            }
        ), 
        Send(
            "trends_researcher" , 
            {
                **state,
                "research_type" : "trends"
            }
        ),
        Send(
            "risks_researcher",
            {
                **state,
                "research_type" : "risks"
            }
        )
    ]