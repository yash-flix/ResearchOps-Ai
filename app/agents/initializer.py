import uuid
from datetime import datetime

from app.graph.state import GraphState


def initializer_node(
    state: GraphState
) -> dict:

    return {
        "execution_id": str(uuid.uuid4()),

        "started_at":
            datetime.utcnow().isoformat(),

        "token_usage": {
            "researcher": 0,
            "analyst": 0,
            "writer": 0,
            "reviewer": 0,
            "evaluator": 0
        },

        "report_version": 0,

        "review_iterations": 0
    }