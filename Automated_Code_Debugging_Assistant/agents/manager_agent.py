from crewai import Agent

def create_manager_agent():
    return Agent(
        role="Manager",
        goal="Ensure accurate and efficient code debugging workflow",
        backstory="Experienced team leader managing developer tasks",
        allow_delegation=True
    )
