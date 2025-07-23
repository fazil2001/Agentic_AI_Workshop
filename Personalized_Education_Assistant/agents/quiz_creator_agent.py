from crewai import Agent

quiz_creator_agent = Agent(
    role="Quiz Creator",
    goal="Generate personalized quizzes for topics",
    backstory="A creative test-maker focused on engaging and insightful questions."
)