from app.llm.factory import get_llm
from app.models.output_models import SupervisorDecision
from app.graph.state import GraphState

llm = get_llm()

structured_llm = llm.with_structured_output(
    SupervisorDecision

)

def build_supervisor_prompt(state:GraphState):
    return f"""
    You are a workflow supervisor.

    Decide which agent should execute next.

    Current Task:
    {state["task"]}

    Research Available:
    {bool(state["research_results"])}

    Analysis Available:
    {bool(state["analysis_results"])}

    Report Available:
    {bool(state["report"])}

    Approved:
    {state["approved"]}

    Review Feedback:
    {state["review_feedback"]}

    Routing Rules:

    1. If research does not exist ->
       web_researcher

    2. If research exists but analysis does not ->
       analyst

    3. If analysis exists but report does not ->
       writer

    4. If report exists but not approved ->
       reviewer

    5. If approved ->
       done

    6. If report exists and approved == False and review_feedback exists → writer
    """

def supervisor_node(state : GraphState):
    prompt = build_supervisor_prompt(state)
    decision = structured_llm.invoke(prompt)

    return {
        "next_agent" : decision.next_agent
    }