from langgraph.graph import StateGraph , START , END

from app.graph.state import GraphState

from app.memory.checkpointer import memory

#import nodes 
from app.agents.supervisor import supervisor_node
from app.agents.web_researcher import web_researcher_node
from app.agents.analyst import analyst_node
from app.agents.writer import writer_node
from app.agents.reviewer import reviewer_node
from app.agents.evaluator import evaluator_node 
from app.agents.initializer import initializer_node

#parallel search 
from app.agents.research_planner import planner_node
from app.agents.facts_researcher import (
    facts_researcher_node
)

from app.agents.trends_researcher import (
    trends_researcher_node
)

from app.agents.risks_researcher import (
    risks_researcher_node
)

from app.graph.research_router import (
    research_router
)

# Import routers 
from app.graph.router import (
    supervisor_router
)

workflow = StateGraph(GraphState)

# required nodes in the workflow 

#research nodes
workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "facts_researcher",
    facts_researcher_node
)

workflow.add_node(
    "trends_researcher",
    trends_researcher_node
)

workflow.add_node(
    "risks_researcher",
    risks_researcher_node
)



workflow.add_node(
    "supervisor" , 
    supervisor_node
)



workflow.add_node(
    "analyst",
    analyst_node
)

workflow.add_node(
    "writer",
    writer_node
)

workflow.add_node(
    "reviewer",
    reviewer_node
)
workflow.add_node(
    "evaluator",
    evaluator_node
)
workflow.add_node(
    "initializer",
    initializer_node
)

#edges of the graph/workflow
workflow.add_edge(
    START,
    "initializer"
)

workflow.add_edge(
    "initializer",
    "supervisor"
)

workflow.add_conditional_edges(
    "supervisor",
    supervisor_router,
    {
        "planner": "planner",
        "analyst": "analyst",
        "writer": "writer",
        "reviewer": "reviewer",
        "evaluator": "evaluator",
        "__end__": END
    }
)
workflow.add_conditional_edges(
    "planner",
    research_router
)

workflow.add_edge(
    [
        "facts_researcher",
        "trends_researcher",
        "risks_researcher"
    ],
    "analyst"
)

workflow.add_edge(
    "analyst",
    "supervisor"
)
workflow.add_edge(
    "writer",
    "supervisor"
)

workflow.add_edge(
    "reviewer",
    "supervisor"
)

workflow.add_edge(
    "evaluator",
    "supervisor"
)

graph = workflow.compile(checkpointer = memory )