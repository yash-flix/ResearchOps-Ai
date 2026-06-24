from app.llm.factory import get_fast_llm

from app.models.review_models import (
    ReviewDecision
)

from app.graph.state import GraphState
from app.config.logger import logger
from langsmith import traceable


def build_review_prompt(task:str , report :str):
    return f"""
You are a senior quality reviewer.

Review the report carefully.

Task:
{task}

Report:
{report}

Evaluate:

1. Completeness
2. Accuracy
3. Clarity
4. Actionability
5. Professionalism

Return:

approved: true or false

feedback: concise review comments

Do not return routing decisions.
Do not mention next_agent.
"""

fast_llm = get_fast_llm()

review_llm = fast_llm.with_structured_output(
    ReviewDecision
)


@traceable(name="reviewer")
def reviewer_node(state:GraphState)->dict:

    
    prompt = build_review_prompt(
        task = state["task"],
        report = state["report"] 
        )
    decision = review_llm.invoke(prompt)

    logger.info(
    f"Reviewer decision: approved={decision.approved}"
)
    logger.info("REVIEWER EXECUTED")

    if decision.approved:
        
        return {
            "approved" : True , 
            "review_feedback" :decision.feedback,
            "review_iterations": state["review_iterations"] + 1,
            "next_agent": "supervisor"
        }
    return {
            "approved" :False , 
            "review_feedback" :decision.feedback,
            "review_iterations": state["review_iterations"] + 1,
            "next_agent": "supervisor"
        }
