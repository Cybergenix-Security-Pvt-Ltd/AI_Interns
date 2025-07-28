from langchain.tools import tool

@tool
def weather_tool(city: str) -> str:     # Type the city name give weather 
    return f"The weather in {city} is sunny with 30°C."

