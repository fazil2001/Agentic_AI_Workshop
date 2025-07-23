from crewai import Task

def create_correction_task(agent, code_input):
    return Task(
        description="Fix the Python code errors identified in the analysis step.",
        expected_output="A corrected version of the original Python code.",
        agent=agent,
        input=code_input
    )
