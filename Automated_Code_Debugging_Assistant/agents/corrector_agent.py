from crewai import Agent

def create_corrector_agent():
    return Agent(
        role="Code Corrector",
        goal="Fix syntax and logic errors in Python code",
        backstory="Expert Python developer known for code debugging",
        allow_delegation=False
    )
