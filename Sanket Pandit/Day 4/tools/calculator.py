from langchain.tools import tool

@tool
def calculator_tool(expression: str) -> str:  # if your any expression calculate
    try:                                       
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

