from crewai import Task
from agents.project_idea_agent import project_idea_agent

project_task = Task(
    description="Suggest project ideas based on expertise level",
    agent=project_idea_agent,
    expected_output="ProjectIdea"
)