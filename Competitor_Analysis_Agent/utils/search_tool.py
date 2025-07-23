from langchain.tools import Tool
from langchain.utilities.google_search import GoogleSearchAPIWrapper

def get_search_tool():
    search = GoogleSearchAPIWrapper()
    return Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions about current events or data on businesses, such as footfall, busy times, or competitor locations"
    )
