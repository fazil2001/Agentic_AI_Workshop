from autogen import UserProxyAgent

def create_user_proxy_agent(group_manager):
    return UserProxyAgent(
        name="user_proxy_agent",
        human_input_mode="NEVER",
        code_execution_config=False,
        default_auto_reply="User has uploaded the bill image. Please process it.",
        llm_config=False,
        is_termination_msg=lambda x: "summary" in x.get("content", "").lower()
    )
