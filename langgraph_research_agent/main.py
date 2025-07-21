from langgraph_workflow import build_graph, run_query

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    graph = build_graph()
    result = run_query(graph, user_query)
    print("\nFinal Response:\n", result)
