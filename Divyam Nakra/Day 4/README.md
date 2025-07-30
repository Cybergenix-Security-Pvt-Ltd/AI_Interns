# 🤖 SmartToolAgent

SmartToolAgent is a beginner-friendly Python project that uses **LangChain** and **Groq's DeepSeek model** to build a smart agent that can:
- 🧮 Solve math expressions
- 🌤️ Give (mock) weather updates
- 🧩 Be extended with new tools by just dropping them into a folder


## 🚀 Getting Started

1. **Clone this repo**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your API key**  
Edit the `.env` file and add:
```
GROQ_API_KEY=your_groq_key_here
```

4. **Run the agent**
```bash
python main.py
```

Try asking:
- `What's 15 * 3 + 2?`
- `What's the weather in Delhi?`

---

## 🔌 Add Your Own Tools

1. Go to `toolbox/`
2. Create a new Python file like `joke_tool.py`
3. Use the `@tool` decorator and return something
4. Import the tool in `main.py` and add it to the `tools=[...]` list

---

