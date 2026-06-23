from datetime import datetime


def finalizer_node(state):

    started = datetime.fromisoformat(
        state["started_at"]
    )

    finished = datetime.utcnow()

    duration = (
        finished - started
    ).total_seconds()

    return {
        "finished_at":
            finished.isoformat(),

        "duration_seconds":
            duration
    }