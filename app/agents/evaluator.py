from app.graph.state import GraphState
from app.llm.factory import get_llm

from app.models.evaluation_models import (
    EvaluationResult
)

def build_evaluation_prompt(
    task: str,
    research_results: str,
    analysis_results: str,
    report: str
):

    return f"""
You are an expert AI evaluation judge.

Evaluate the quality of this workflow.

Original Task:
{task}

Research Results:
{research_results}

Analysis Results:
{analysis_results}

Final Report:
{report}

Score each category from 0 to 10.

Evaluation Criteria:

1. Research Quality
   - Depth
   - Relevance
   - Accuracy

2. Analysis Quality
   - Insightfulness
   - Business Value
   - Reasoning

3. Report Quality
   - Structure
   - Clarity
   - Professionalism

4. Faithfulness
   - Grounded in research
   - No unsupported claims

5. Completeness
   - Fully addresses task

Provide concise reasoning.
"""


llm = get_llm()

evaluation_llm = llm.with_structured_output(
    EvaluationResult
)

def evaluator_node(state:GraphState)->dict:
    prompt = build_evaluation_prompt(
    task=state["task"],
    research_results=state["research_results"],
    analysis_results=state["analysis_results"],
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