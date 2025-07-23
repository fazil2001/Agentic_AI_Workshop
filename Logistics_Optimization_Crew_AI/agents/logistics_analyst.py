from crewai import Agent

def create_logistics_analyst():
    return Agent(
        role="Logistics Analyst",
        goal="Analyze current logistics operations to identify inefficiencies in delivery routes and inventory turnover.",
        backstory="You are a logistics expert who understands transportation trends, warehouse efficiency, and routing challenges.",
        verbose=True
    )
