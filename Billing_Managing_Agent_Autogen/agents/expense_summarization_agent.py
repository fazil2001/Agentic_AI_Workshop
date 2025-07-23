from autogen import AssistantAgent

def create_expense_summarization_agent(tool):
    return AssistantAgent(
        name="expense_summarization_agent",
        llm_config={"config_list": tool},
        description="Summarizes expenses by category and highlights unusual trends."
    )
