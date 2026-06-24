from app.graph.workflow import graph
from app.config.export import save_report
import uuid

result = graph.invoke(
    {
        "task": "Research the impact of AI agents on software engineering",
        "raw_research_context" : "" ,
        "research_results": [],
        "analysis_results": "",
        "report": "",
        "review_feedback": "",
        "evaluation_results": {},
        "approved": False,
        "retry_count": 0,
        "next_agent": ""
    },
    config={
        "configurable": {
            "thread_id": str(uuid.uuid4())
        }
    }
)
save_report(result)
print(result)