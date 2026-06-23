from pydantic import BaseModel, Field


class EvaluationResult(BaseModel):

    research_score: float = Field(
        ge=0,
        le=10
    )

    analysis_score: float = Field(
        ge=0,
        le=10
    )

    report_score: float = Field(
        ge=0,
        le=10
    )

    faithfulness_score: float = Field(
        ge=0,
        le=10
    )

    completeness_score: float = Field(
        ge=0,
        le=10
    )

    overall_score: float = Field(
        ge=0,
        le=10
    )

    reasoning: str