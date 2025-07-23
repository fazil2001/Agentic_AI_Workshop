import os
from dotenv import load_dotenv
from crewai import Crew
from tasks.generate_material_task import material_task
from tasks.create_quiz_task import quiz_task
from tasks.suggest_project_task import project_task
from tools.project_suggestion_tool import ProjectSuggestionTool

load_dotenv()

crew = Crew(
    tasks=[material_task, quiz_task, project_task],
    tools=[ProjectSuggestionTool()],
    process="sequential"
)

output = crew.run({
    "topics": ["machine learning", "data structures"],
    "expertise": "intermediate"
})

print("\n===== Final Output =====")
print(output)
