from typing import Literal
from pydantic import BaseModel

class ReviewDecision(BaseModel):
    approved: bool
    feedback: str
    next_agent: Literal["writer", "supervisor"]