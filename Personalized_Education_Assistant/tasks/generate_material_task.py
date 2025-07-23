from crewai import Task
from agents.learning_material_agent import learning_material_agent

material_task = Task(
    description="Generate learning materials for user topics",
    agent=learning_material_agent,
    expected_output="LearningMaterial"
)