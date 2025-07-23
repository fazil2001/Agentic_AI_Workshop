from config import gemini_api_key
from tools import plus, subtract, multiply, divide
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
import re

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key)

def is_math_query(input_str):
    return any(op in input_str.lower() for op in ["plus", "add", "minus", "subtract", "multiply", "times", "divide"])

def extract_numbers(input_str):
    return list(map(float, re.findall(r"\d+(?:\.\d+)?", input_str)))

class AgentState(dict):
    pass

def chatbot_node(state: AgentState):
    query = state["query"]
    if is_math_query(query):
        return {"type": "math"}
    response = llm.invoke(query)
    return {"response": response.content, "type": "done"}

def math_node(state: AgentState):
    query = state["query"].lower()
    numbers = extract_numbers(query)
    if len(numbers) < 2:
        return {"response": "Please provide two numbers.", "type": "done"}
    a, b = numbers[:2]
    if "plus" in query or "add" in query:
        result = plus.invoke({"a": a, "b": b})
    elif "minus" in query or "subtract" in query:
        result = subtract.invoke({"a": a, "b": b})
    elif "multiply" in query or "times" in query:
        result = multiply.invoke({"a": a, "b": b})
    elif "divide" in query:
        result = divide.invoke({"a": a, "b": b})
    else:
        result = "Operation not recognized."
    return {"response": f"The result is: {result}", "type": "done"}

# Build the LangGraph
workflow = StateGraph(AgentState)
workflow.add_node("chatbot", chatbot_node)
workflow.add_node("math", math_node)
workflow.set_entry_point("chatbot")
workflow.add_conditional_edges("chatbot", lambda x: x["type"], {"math": "math", "done": END})
workflow.add_edge("math", END)
app = workflow.compile()
