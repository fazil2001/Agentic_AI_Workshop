from crewai import Task

def define_logistics_analysis_task(agent, product_list):
    return Task(
        description=f"Research and analyze logistics performance for the following product categories: {', '.join(product_list)}. Focus on delivery delays, routing inefficiencies, and inventory issues.",
        expected_output="A comprehensive report on logistics inefficiencies and trends.",
        agent=agent
    )
