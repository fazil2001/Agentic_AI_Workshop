from agents.group_chat_manager import group_chat_manager

class UserProxyAgent:
    def initiate(self):
        print("User: I want help managing my investments.")
        group_chat_manager.start()

user_proxy_agent = UserProxyAgent()