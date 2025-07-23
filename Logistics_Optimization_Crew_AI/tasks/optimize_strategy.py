from crewai import Task

def define_optimization_task(agent, product_list):
    return Task(
        description=f"Based on the logistics analysis, design optimization strategies for these product categories: {', '.join(product_list)}. Include route planning, warehouse stocking strategies, and time savings estimation.",
        expected_output="An actionable optimization strategy that enhances logistics efficiency.",
        agent=agent
    )
