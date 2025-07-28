
# 🤖 Modular LangChain Agent

This project is a **LangChain-powered conversational agent** that uses a **Groq LLM** (with DeepSeek model) and integrates multiple tools like:

- 🔢 Calculator  
- 🌦️ Weather  
- 📚 Wikipedia  
- 🧠 Agent reasoning with ReAct  
- 🖥️ Streamlit frontend for user interaction

---

## 📂 Project Structure

```
Day4_task/
│
├── app.py                    # Streamlit UI
├── main.py                   # Terminal CLI interface
├── agents/
│   └── tool_agent.py         # Initializes the agent with tools
├── tools/
│   ├── calculator.py         # Arithmetic function
│   ├── weather.py            # OpenWeather API
│   └── wiki.py               # Wikipedia search
└── llm/
    └── groq_llm.py           # Groq API integration
```

---

## 🔧 Setup & Installation

### 1. ⚙️ Clone the repository
```bash
git clone <your-repo-url>
cd Day4_task
```

### 2. 🐍 Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. 📦 Install dependencies
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, here are the essentials:

```bash
pip install langchain openai langchain-openai langchainhub streamlit wikipedia requests
```

---

## 🔑 API Keys Required

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
```

Or export using terminal:

```bash
$env:GROQ_API_KEY="your_key"         # PowerShell (Windows)
export GROQ_API_KEY="your_key"       # macOS/Linux
```

---

## 🚀 Running the Agent

### 1. 🧪 CLI Mode (Terminal)
```bash
python main.py
```

### 2. 🖥️ UI Mode (Streamlit App)
```bash
streamlit run app.py
```

---

## 🧩 Tools Included

| Tool Name     | Purpose                                      |
|---------------|----------------------------------------------|
| `calculate()` | Handles arithmetic operations                |
| `get_weather()` | Fetches weather using OpenWeather API      |
| `wikipedia_search()` | Fetches brief info from Wikipedia     |

---

## 🧠 Agent Logic

- Uses **LangChain ReAct agent**
- Powered by **Groq LLM (deepseek-coder:7b)**
- Each tool is auto-called based on LLM reasoning
- Uses `.run()` to invoke agent
- Handles output parsing errors gracefully

---

## 🌐 Example Queries

```
🧮 3 + 7 * (2 + 1)
🌦️ What is the weather in Solapur?
📚 Who discovered gravity?
📜 Who invented zero?
```

---

## 🙌 Author

Built by **Yessha Bapna** as part of the **AI Developer Internship Task** at **Cybergenix Pvt Ltd**.

---

## 📃 License

MIT License. Feel free to fork and expand.
