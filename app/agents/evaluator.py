from app.graph.state import GraphState
from app.llm.factory import get_llm

from app.models.evaluation_models import (
    EvaluationResult
)

def build_evaluation_prompt(
    task: str,
    report: str
):

   return f"""
You are an expert AI evaluation judge.

Original Task:
{task}

Final Report:
{report}

Evaluate and assign scores from 0-10 for:

1. Research Score
   - Evidence of strong supporting research

2. Analysis Score
   - Depth of reasoning and insight

3. Report Score
   - Structure, clarity, professionalism

4. Faithfulness Score
   - No unsupported claims
   - Consistent with provided information

5. Completeness Score
   - Fully addresses the task

6. Overall Score
   - Overall quality of the output

Provide concise reasoning.
"""


llm = get_llm()

evaluation_llm = llm.with_structured_output(
    EvaluationResult
)

def evaluator_node(state:GraphState)->dict:
    prompt = build_evaluation_prompt(
    task=state["task"],
    report=state["report"]
)
    
    evaluation = evaluation_llm.invoke(prompt)

    return {
    "evaluation_results": {
        "research_score":
            evaluation.research_score,

        "analysis_score":
            evaluation.analysis_score,

        "report_score":
            evaluation.report_score,

        "faithfulness_score":
            evaluation.faithfulness_score,

        "completeness_score":
            evaluation.completeness_score,

        "overall_score":
            evaluation.overall_score,

        "reasoning":
            evaluation.reasoning
    },

    "next_agent": "supervisor"
}