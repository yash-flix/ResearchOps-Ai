from langgraph.constants import Send


def research_router(state):

    return [
        Send(
            "facts_researcher",
            state
        ),
        Send(
            "trends_researcher",
            state
        ),
        Send(
            "risks_researcher",
            state
        )
    ]