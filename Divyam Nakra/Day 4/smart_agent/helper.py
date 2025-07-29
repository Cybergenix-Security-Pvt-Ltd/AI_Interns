import os
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq

def build_smart_agent(tools):
    # Load your Groq API Key
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Initialize the Groq LLM with DeepSeek
    llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="deepseek-coder:7b")

    # Initialize a zero-shot agent that can pick the right tool
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
