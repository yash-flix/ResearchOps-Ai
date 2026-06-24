from app.graph.state import GraphState
from app.llm.factory import get_llm
from langsmith import traceable
from app.config.logger import logger
from app.config.constants import MAX_RESEARCH_CHARS

llm = get_llm()


def build_analysis_prompt(
    task: str,
    research_results: str
):

    return f"""
You are a senior business analyst.

Task:
{task}

Research Findings:
{research_results}

Provide:

1. Executive Summary
2. Key Findings
3. Opportunities
4. Risks
5. Emerging Trends
6. Strategic Recommendations

Focus on actionable insights.
"""

@traceable(name="analyst")
def analyst_node(
    state: GraphState
) -> dict:
    
    combined_research = "\n\n".join(
    state["research_results"]
     )[:MAX_RESEARCH_CHARS]

    prompt = build_analysis_prompt(
        task=state["task"],
        research_results=combined_research
    )
    logger.info(
    f"Analyst input size: {len(combined_research)} chars"
)

    analysis = llm.invoke(prompt)

    tokens = (
    analysis
    .response_metadata
    .get("token_usage", {})
    .get("total_tokens", 0)
)
    logger.info("ANALYST EXECUTED")

    return {
        "analysis_results":
            analysis.content ,  

         "token_usage": {
        **state["token_usage"],
        "analyst": tokens
    },
         "next_agent": "supervisor"
    }