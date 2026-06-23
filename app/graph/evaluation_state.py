from typing import TypedDict

class EvaluationState(TypedDict):
    research_score: float
    analysis_score: float
    report_score: float
    faithfulness_score: float
    completeness_score: float
    overall_score: float
    reasoning: str