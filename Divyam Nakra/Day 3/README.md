# 💻 AutoCode Bot

AutoCode Bot is a beginner-friendly coding assistant that generates clean, simple code based on what you ask in plain English. It uses LLaMA 3 via Groq's fast API.

---

## 🌟 Features

- Ask anything in plain English like:  
  👉 “Create a Python calculator”  
  👉 “Make a program to check prime number”  
- It will generate **well-commented code** a beginner can understand.
- Built with **Streamlit** for a simple UI.

---

## 🧠 How it works

AutoCode Bot sends your question to the **Groq AI model**, which replies with Python code.
The system prompt ensures the code is always clean and beginner-friendly.

---

## 🚀 How to Run

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/autocode-bot.git
   cd autocode-bot
   ```

2. **Install requirements**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**  
   Create a file at `.streamlit/secrets.toml` and add:

   ```toml
   GROQ_API_KEY = "your_groq_api_key"
   ```

   You can get your key here: [https://console.groq.com/keys](https://console.groq.com/keys)

4. **Run the app**  
   ```bash
   streamlit run autocode_bot.py
   ```

---

## 📷 Preview

![screenshot](https://dummyimage.com/800x400/ddd/333&text=AutoCode+Bot+Preview)

---

## 🛠 Built With

- Python
- Streamlit
- Groq API
