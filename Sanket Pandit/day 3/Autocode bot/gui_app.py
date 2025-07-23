import streamlit as st
from gpt_handler import generate_code
from file_writer import write_code_to_file
from launcher import open_in_editor
from utils import detect_language_from_prompt
import base64
import os

st.set_page_config(page_title="AutoCode Bot", layout="centered")
st.title("🤖 AutoCode Bot")

prompt = st.text_area("🧠 Enter your coding task:", height=150)

if st.button("Generate Code") and prompt:
    st.info("⏳ Generating code...")
    code = generate_code(prompt)
    language = detect_language_from_prompt(prompt)
    filepath = write_code_to_file(code, language)

    st.success("✅ Code Generated and Saved!")
    st.code(code, language=language)

    with open(filepath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filepath.split(os.sep)[-1]}">📥 Download Code File</a>'
        st.markdown(href, unsafe_allow_html=True)
