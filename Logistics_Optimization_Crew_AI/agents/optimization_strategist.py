from crewai import Agent

def create_optimization_strategist():
    return Agent(
        role="Optimization Strategist",
        goal="Develop optimized strategies based on logistics data to reduce delivery time and improve inventory performance.",
        backstory="You are a strategist who uses data-driven insights to improve logistics workflows.",
        verbose=True
    )
