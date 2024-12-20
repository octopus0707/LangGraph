

from typing import List
from typing_extensions import TypedDict

from langgraph.graph import END, StateGraph, START
from langchain.schema import Document
from langchain_core.output_parsers import StrOutputParser

from langgraph.graph import START, END, StateGraph

from gather_user_info_agent.state import AgentState
from gather_user_info_agent.nodes.generation import generate
from gather_user_info_agent.nodes.grade_documents import docs_grader_llm
from gather_user_info_agent.nodes.grade_question import grade_documents
from gather_user_info_agent.nodes.retriever import retrieve
from gather_user_info_agent.nodes.rewrite import transform_query
from gather_user_info_agent.nodes.web_search import web_search
from gather_user_info_agent.consts import RETRIEVE_NODE, GRADE_DOCUMENTS_NODE, GENERATE_NODE, TRANSFORM_QUERY_NODE, WEB_SEARCH_NODE

from gather_user_info_agent.edges.conditional_edges import decide_to_generate

import os
from dotenv import load_dotenv
load_dotenv(override=True)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

workflow = StateGraph(AgentState)
# Define the nodes
workflow.add_node(RETRIEVE_NODE, retrieve)  # retrieve
workflow.add_node(GRADE_DOCUMENTS_NODE, grade_documents)  # grade documents
workflow.add_node(GENERATE_NODE, generate)  # generatae
workflow.add_node(TRANSFORM_QUERY_NODE, transform_query)  # transform_query
workflow.add_node(WEB_SEARCH_NODE, web_search)  # web search

# Build graph
workflow.add_edge(START, RETRIEVE_NODE)
workflow.add_edge(RETRIEVE_NODE, GRADE_DOCUMENTS_NODE)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS_NODE,
    decide_to_generate,
    {
        "transform_query": TRANSFORM_QUERY_NODE,
        "generate": GENERATE_NODE,
    },
)
workflow.add_edge(TRANSFORM_QUERY_NODE, WEB_SEARCH_NODE)
workflow.add_edge(WEB_SEARCH_NODE, GENERATE_NODE)
workflow.add_edge(GENERATE_NODE, END)

# Compile
app = workflow.compile()