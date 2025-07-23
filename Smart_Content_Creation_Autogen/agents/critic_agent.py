from utils.gemini_wrapper import GeminiClient

class ContentCriticAgent:
    def __init__(self):
        self.role = "You are the Content Critic Agent. Your role is to evaluate the content drafted by the Content Creator Agent. Provide feedback on language and technical correctness, and suggest improvements."
        self.llm = GeminiClient()

    def give_feedback(self, content):
        prompt = f"{self.role}\nPlease review the following content and provide feedback:\n{content}"
        return self.llm.generate_content(prompt)
