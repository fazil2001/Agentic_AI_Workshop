from autogen import GroupChat, GroupChatManager
from agents.user_proxy_agent import create_user_proxy_agent
from agents.bill_processing_agent import create_bill_processing_agent
from agents.expense_summarization_agent import create_expense_summarization_agent
from tools.gemini_tool import get_gemini_config

def run():
    gemini_tool = get_gemini_config()

    user_proxy_agent = create_user_proxy_agent("group_manager")
    bill_processing_agent = create_bill_processing_agent(gemini_tool)
    expense_summary_agent = create_expense_summarization_agent(gemini_tool)

    group_chat = GroupChat(
        agents=[user_proxy_agent, bill_processing_agent, expense_summary_agent],
        messages=[],
        max_round=10
    )

    manager = GroupChatManager(
        groupchat=group_chat,
        llm_config={"config_list": gemini_tool}
    )

    user_proxy_agent.initiate_chat(manager, message="Here is the image of the bill I want to track.")

if __name__ == "__main__":
    run()
