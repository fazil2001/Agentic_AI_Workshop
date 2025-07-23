from crewai import Agent
from tools.code_interpreter import CodeInterpreterTool

def create_analyzer_agent():
    return Agent(
        role="Code Analyzer",
        goal="Identify syntax and logical errors in Python code",
        backstory="Expert in Python code analysis and error detection",
        tools=[CodeInterpreterTool()],
        allow_delegation=False
    )
