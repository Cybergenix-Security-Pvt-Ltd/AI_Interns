# main.py

from agents.tool_agent import get_agent

def main():
    print("🤖 Modular LangChain Agent (Groq + DeepSeek)")
    print("Type your query or 'exit' to quit.")
    agent = get_agent()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        try:
            response = agent.run(user_input)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
