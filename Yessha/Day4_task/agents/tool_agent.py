# agents/tool_agent.py

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from tools.wikipedia_search import search_wikipedia
from llm.groq_llm import get_llm

# Import tools directly
from tools.calculator import calculate
from tools.weather import get_weather

def get_agent():
    llm = get_llm()

    tools = [
        Tool.from_function(
            func=calculate,
            name="Calculator",
            description="Useful for answering math-related questions using arithmetic operations."
        ),
        Tool.from_function(
            func=get_weather,
            name="GetWeather",
            description="Provides current weather information for a given city."
        ),
         Tool.from_function(
        func=search_wikipedia,
        name="WikipediaSearch",
        description="Useful for fetching encyclopedic information about a topic from Wikipedia."
    )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent
