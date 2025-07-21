import openai
import os
openai.api_key = os.getenv("GOOGLE_API_KEY")

def summarize_node(state):
    query = state["query"]
    info = state["info"]
    prompt = f"""
    Summarize the following information to answer the query:

    Query: {query}

    Info:
    {info}

    Summary:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()