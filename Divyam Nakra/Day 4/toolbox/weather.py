from langchain.tools import tool

@tool
def get_weather_info(location: str) -> str:
    """Returns a fake weather report for the given city (demo purpose)."""
    return f"The weather in {location} is sunny with 30°C."  # Replace with real API if needed
