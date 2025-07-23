from crewai import Crew
from config import get_api_key
from agents.logistics_analyst import create_logistics_analyst
from agents.optimization_strategist import create_optimization_strategist
from tasks.analyze_logistics import define_logistics_analysis_task
from tasks.optimize_strategy import define_optimization_task

def main():
    product_list = ["Consumer Electronics", "Groceries", "Medical Supplies"]

    # Initialize agents
    analyst = create_logistics_analyst()
    strategist = create_optimization_strategist()

    # Define tasks
    task1 = define_logistics_analysis_task(analyst, product_list)
    task2 = define_optimization_task(strategist, product_list)

    # Build the Crew
    crew = Crew(
        agents=[analyst, strategist],
        tasks=[task1, task2],
        verbose=True
    )

    result = crew.kickoff()
    print("\n\nFinal Optimization Strategy:\n")
    print(result)

if __name__ == "__main__":
    main()
