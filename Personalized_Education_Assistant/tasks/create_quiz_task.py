from crewai import Task
from agents.quiz_creator_agent import quiz_creator_agent

quiz_task = Task(
    description="Create personalized quizzes for user topics",
    agent=quiz_creator_agent,
    expected_output="Quiz"
)