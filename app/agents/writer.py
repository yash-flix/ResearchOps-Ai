from app.graph.state import GraphState
from app.llm.factory import get_llm

llm = get_llm()

def build_writer_prompt(task:str , research_results:str , analysis_results:str , review_feedback: str)->str:
    return f"""
You are a senior business consultant.

Your job is to create a polished executive report.

Task:
{task}

Research Findings:
{research_results}

Analysis:
{analysis_results}

Review Feedback:
{review_feedback}

Create a professional report using the following structure:

# Executive Summary

# Background

# Key Findings

# Strategic Analysis

# Recommendations

# Conclusion

Requirements:

- Professional tone
- Clear structure
- Concise but informative
- Business-focused language
- Use markdown formatting
- Do not invent facts
- Base conclusions only on the provided information
"""

def writer_node(state:GraphState)->dict:
    prompt = build_writer_prompt(
        task = state["task"],
        research_results=state["research_results"],
        analysis_results=state["analysis_results"] ,
        review_feedback=state.get("review_feedback", "")
            
    )
    result = llm.invoke(prompt)

    return {
        "report" : result.content ,
        "next_agent" : "supervisor"
    }
