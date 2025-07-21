from serpapi import GoogleSearch
import os

def web_node(state):
    query = state["query"]
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY")
    })
    result = search.get_dict()
    snippets = [item["snippet"] for item in result.get("organic_results", [])[:3]]
    return {"query": query, "info": " ".join(snippets)}