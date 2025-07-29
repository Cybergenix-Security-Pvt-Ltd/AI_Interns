from smart_agent.helper import build_smart_agent
from toolbox.calculator import solve_expression
from toolbox.weather import get_weather_info

# Build the agent with tools
agent = build_smart_agent(tools=[solve_expression, get_weather_info])

print("🤖 SmartToolAgent Ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = agent.run(user_input)
    print("🤖", response)
