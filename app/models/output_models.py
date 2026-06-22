from typing import Literal 
from pydantic import BaseModel

class SupervisorDecision(BaseModel):

    next_agent : Literal[  #restrict the orchestrator for only the given agents 
        "web_researcher",
        "rag_researcher",
        "analyst",
        "writer",
        "reviewer",
        "done"
    ]
    reason : str