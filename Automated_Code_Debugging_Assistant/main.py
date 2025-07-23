import os
from crewai import Crew, Process
from agents.analyzer_agent import create_analyzer_agent
from agents.corrector_agent import create_corrector_agent
from agents.manager_agent import create_manager_agent
from tasks.analysis_task import create_analysis_task
from tasks.correction_task import create_correction_task
from dotenv import load_dotenv

load_dotenv()

broken_code = """
def fibonacci_iterative(n):
    if n < 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)
    return fib_sequence
"""

# Create agents
analyzer = create_analyzer_agent()
corrector = create_corrector_agent()
manager = create_manager_agent()

# Create tasks
analysis = create_analysis_task(analyzer, broken_code)
correction = create_correction_task(corrector, broken_code)

# Create crew
crew = Crew(
    agents=[analyzer, corrector, manager],
    tasks=[analysis, correction],
    process=Process.sequential,
    manager=manager,
    planning=True
)

result = crew.kickoff()
print("FINAL OUTPUT:\n", result)
