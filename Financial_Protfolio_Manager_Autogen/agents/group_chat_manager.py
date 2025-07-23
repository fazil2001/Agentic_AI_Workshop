from agents.portfolio_analysis_agent import portfolio_analysis_agent
from workflows.stateflow import state_flow

class GroupChatManager:
    def start(self):
        user_input = portfolio_analysis_agent.analyze()
        state_flow.route(user_input)

group_chat_manager = GroupChatManager()