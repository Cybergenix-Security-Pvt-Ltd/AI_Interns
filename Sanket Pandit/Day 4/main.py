
from agent.agent import create_agent

def main():       # we creating the function to crate one type of agent using while loop give the input and reach to the out
    agent = create_agent()
    print("LangChain Tool Agent ( If you want to exit type 'exit' to quit)")
    while True:
        query = input(">> ")
        if query.lower() in ['exit', 'quit']:
            break
        try:
            result = agent.run(query)
            print("Langchain_Agent_Result", result)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
