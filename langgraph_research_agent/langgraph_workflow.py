from langgraph.graph import StateGraph
from agents.router_agent import router_node
from agents.web_research_agent import web_node
from agents.rag_agent import rag_node
from agents.summarization_agent import summarize_node

def build_graph():
    builder = StateGraph()

    builder.add_node("router", router_node)
    builder.add_node("web", web_node)
    builder.add_node("rag", rag_node)
    builder.add_node("summarize", summarize_node)

    builder.set_entry_point("router")

    builder.add_conditional_edges("router", lambda state: state['route'], {
        "web": "web",
        "rag": "rag"
    })

    builder.add_edge("web", "summarize")
    builder.add_edge("rag", "summarize")
    builder.set_finish_point("summarize")

    return builder.compile()

def run_query(graph, query):
    return graph.invoke({"query": query})