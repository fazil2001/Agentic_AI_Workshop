from utils.gemini_wrapper import GeminiClient

class ContentCreatorAgent:
    def __init__(self):
        self.role = "You are the Content Creator Agent. Your role is to draft content on topics involving Generative AI. Ensure the content is clear, concise, and technically accurate."
        self.llm = GeminiClient()

    def create_draft(self, prompt="Write a brief article about Agentic AI"):
        return self.llm.generate_content(self.role + "\n" + prompt)

    def revise_draft(self, original_draft, feedback):
        revision_prompt = (
            f"{self.role}\nRevise the following draft based on this feedback:\n"
            f"Feedback: {feedback}\nOriginal Draft:\n{original_draft}"
        )
        return self.llm.generate_content(revision_prompt)
