import streamlit as st
import requests  # Send requests to Groq API

# --------------------------
# 🔐 Load API Key from Secrets
# --------------------------
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]  # Put your Groq API key here

# --------------------------
# 🌍 Supported Extensions
# --------------------------
EXTENSIONS = {
    "python": "py",
    "java": "java",
    "c": "c",
    "cpp": "cpp",
    "javascript": "js",
    "html": "html",
    "text": "txt"
}

# --------------------------
# 🧠 System Prompt
# --------------------------
SYSTEM_PROMPT = """You are AutoCode Bot, an expert code generator.
Always give clean code that beginners can easily understand.
Add comments only where needed, and don’t include extra explanations.
Your response must contain only code, nothing else."""

# --------------------------
# 🧠 Call Groq API
# --------------------------
def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",  # Model choice
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --------------------------
# 🌟 Streamlit UI
# --------------------------
st.title("🤖 AutoCode Bot")

query = st.text_area("Ask anything to generate code (e.g., create a calculator in Python)")

lang = st.selectbox("Select language:", list(EXTENSIONS.keys()))

if st.button("Generate Code"):
    if query.strip():
        with st.spinner("Generating..."):
            code = ask_groq(query)
            st.code(code, language=lang)
    else:
        st.warning("Please enter a question first!")
