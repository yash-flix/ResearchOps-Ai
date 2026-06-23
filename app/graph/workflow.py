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

# Import routers 
from app.graph.router import (
    supervisor_router
)

workflow = StateGraph(GraphState)

# required nodes in the workflow 
workflow.add_node(
    "supervisor" , 
    supervisor_node
)

workflow.add_node(
    "web_researcher" ,
    web_researcher_node
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
        "web_researcher": "web_researcher",
        "analyst": "analyst",
        "writer": "writer",
        "reviewer": "reviewer",
        "evaluator": "evaluator",
        "__end__": END
    }
)

workflow.add_edge(
    "web_researcher",
    "supervisor"
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