from typing import Literal 
from pydantic import BaseModel

class SupervisorDecision(BaseModel):

    next_agent : Literal[  #restrict the orchestrator for only the given agents 
        "planner",
        "analyst",
        "writer",
        "reviewer",
        "evaluator",
        "done"
    ]
    reason : str