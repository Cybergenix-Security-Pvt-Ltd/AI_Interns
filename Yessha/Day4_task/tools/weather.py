# tools/weather.py

from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """Returns weather info for a given city (mock data)."""
    mock_weather = {
        "delhi": "Sunny, 35°C",
        "mumbai": "Rainy, 28°C",
        "bangalore": "Cloudy, 25°C"
    }
    city_lower = city.lower()
    return mock_weather.get(city_lower, "Weather data not available for this city.")
