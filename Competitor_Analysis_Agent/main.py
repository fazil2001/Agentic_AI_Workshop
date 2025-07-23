from langchain.chat_models import ChatGooglePalm
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from config import GOOGLE_API_KEY
from utils.search_tool import get_search_tool

def main():
    # Setup
    llm = ChatGooglePalm(google_api_key=GOOGLE_API_KEY, temperature=0.7)
    search_tool = get_search_tool()

    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # Input example (you can also accept dynamic input)
    query = "Top 3 clothing store competitors in Koramangala Bangalore, their footfall and peak hours"

    # Custom prompt
    with open("prompts/report_prompt.txt", "r") as file:
        prompt_template = PromptTemplate(input_variables=["query"], template=file.read())

    final_prompt = prompt_template.format(query=query)

    # Run agent
    print("🔍 Generating Competitor Intelligence Report...\n")
    report = agent.run(final_prompt)
    print("📝 Report:\n")
    print(report)

if __name__ == "__main__":
    main()
