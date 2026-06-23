from app.llm.factory import get_llm

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

If the report is acceptable:

approved = true

If improvements are needed:

approved = false

Provide concise feedback.
"""

llm = get_llm()

review_llm = llm.with_structured_output(
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

    if decision.approved:
        
        return {
            "approved" : True , 
            "review_feedback" :decision.feedback,
            "token_usage": {
            **state["token_usage"],
             "reviewer": tokens
          },
            "next_agent": "supervisor"
        }
    return {
            "approved" :False , 
            "review_feedback" :decision.feedback,
            "next_agent": "supervisor"
        }
