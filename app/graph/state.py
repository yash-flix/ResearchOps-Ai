from typing import TypedDict , Annotated, NotRequired
from app.graph.evaluation_state import EvaluationState
import operator

class GraphState(TypedDict):
    task: str
    research_results: Annotated[list , operator.add]
    analysis_results: str
    report: str

    review_feedback: str
    evaluation_results:  NotRequired[EvaluationState]

    approved: bool
    retry_count: int
    next_agent: str
    error: NotRequired[str]

    execution_id: str
    started_at: str
    finished_at: str
    duration_seconds: float

    token_usage: dict

    report_version: int
    review_iterations: int