from langchain.tools import tool

@tool
def solve_expression(expression: str) -> str:
    """Solves a basic math expression like '15 * 3 + 2'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error solving expression: {e}"
