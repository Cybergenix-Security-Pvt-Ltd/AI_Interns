import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGroq(
        groq_api_key=os.getenv("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"),  # using grok api key 
        model="llama3-8b-8192"

    )
