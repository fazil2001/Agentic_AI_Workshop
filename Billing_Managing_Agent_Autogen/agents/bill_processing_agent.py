from autogen import AssistantAgent

def create_bill_processing_agent(tool):
    return AssistantAgent(
        name="bill_processing_agent",
        llm_config={"config_list": tool},
        description="Extracts and categorizes expenses from bill images."
    )
