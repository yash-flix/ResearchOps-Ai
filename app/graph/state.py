from typing import TypedDict , Any 
from app.graph.evaluation_state import EvaluationState

class GraphState(TypedDict):
    task: str
    research_results: str
    analysis_results: str
    report: str

    review_feedback: str
    evaluation_results: EvaluationState

    approved: bool
    retry_count: int
    next_agent: str