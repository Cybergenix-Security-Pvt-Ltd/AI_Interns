# app.py

import streamlit as st
from agents.tool_agent import get_agent

st.set_page_config(page_title="LangChain Modular Agent", page_icon="🤖")
st.title("🤖 Modular LangChain Agent")
st.write("Ask me anything ...")

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = get_agent()
if "response" not in st.session_state:
    st.session_state.response = ""
if "query" not in st.session_state:
    st.session_state.query = ""

# Layout: 3 columns (query input + submit + clear)
col1, col2, col3 = st.columns([5, 1, 1])  # Wide input, narrow buttons

with col1:
    st.session_state.query = st.text_input("Enter your query:", value=st.session_state.query, label_visibility="collapsed")

with col2:
    if st.button("Submit"):
        if st.session_state.query.strip():
            with st.spinner("Thinking..."):
                try:
                    st.session_state.response = st.session_state.agent.run(st.session_state.query)
                except Exception as e:
                    st.session_state.response = f"❌ Error: {str(e)}"

with col3:
    if st.button("Clear"):
        st.session_state.query = ""
        st.session_state.response = ""

# Display response
if st.session_state.response:
    st.markdown("### 🤖 Response:")
    st.write(st.session_state.response)
