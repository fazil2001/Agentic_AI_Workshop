from langchain.tools import tool

@tool
def plus(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract second number from first."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide first number by second."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b