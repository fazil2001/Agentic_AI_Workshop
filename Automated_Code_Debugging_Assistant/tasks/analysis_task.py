from crewai import Task

def create_analysis_task(agent, code_input):
    return Task(
        description="Analyze the provided Python code and identify all syntax or logic issues.",
        expected_output="A detailed list of errors found in the code.",
        agent=agent,
        input=code_input
    )
