from app.llm.factory import get_llm
from app.models.output_models import SupervisorDecision
from app.graph.state import GraphState
from langsmith import traceable

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
{bool(state.get("research_results"))}

Analysis Available:
{bool(state.get("analysis_results"))}

Report Available:
{bool(state.get("report"))}

Review Feedback:
{state.get("review_feedback", "")}

Evaluation Available:
{bool(state.get("evaluation_results"))}

 Routing Rules:
1. No research
   → web_researcher

2. Research exists but no analysis
   → analyst

3. Analysis exists but no report
   → writer

4. Report exists and not approved
   → reviewer

5. Approved and no evaluation
   → evaluator

6. Approved and evaluation exists
   → done
    """

@traceable(name="supervisor")
def supervisor_node(state : GraphState):
    prompt = build_supervisor_prompt(state)
    decision = structured_llm.invoke(prompt)


    return {
        "next_agent" : decision.next_agent
    }