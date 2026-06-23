# app/graph/state.py

from typing import TypedDict


class GraphState(TypedDict):

    task: str

    research_results: str

    analysis_results: str

    report: str

    review_feedback: str

    next_agent: str

    retry_count: int

    approved: bool

    report_version: int

    review_iterations: int