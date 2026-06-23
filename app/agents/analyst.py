from app.graph.state import GraphState
from app.llm.factory import get_llm
from langsmith import traceable

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

    prompt = build_analysis_prompt(
        task=state["task"],
        research_results=state["research_results"]
    )

    analysis = llm.invoke(prompt)

    return {
        "analysis_results":
            analysis.content , 
         "next_agent": "supervisor"
    }