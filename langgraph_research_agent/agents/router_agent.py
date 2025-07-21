def router_node(state):
    query = state["query"].lower()
    if any(keyword in query for keyword in ["latest", "current", "today"]):
        return {"route": "web", "query": query}
    else:
        return {"route": "rag", "query": query}