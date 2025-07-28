from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import Tool
from llm.groq_llm import get_llm
from tools import all_tools  #  using this we are import list of tools

def create_agent():
    llm = get_llm()

    return initialize_agent(
        tools=all_tools,  # in this we are passing the tools like calculate and weather 
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
