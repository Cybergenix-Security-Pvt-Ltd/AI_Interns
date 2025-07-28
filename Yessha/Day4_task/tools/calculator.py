# tools/calculator.py

from langchain.tools import tool

@tool
def calculate(expression: str) -> str:
    """Evaluates a basic math expression. Example: 15 * 3 + 2"""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"
