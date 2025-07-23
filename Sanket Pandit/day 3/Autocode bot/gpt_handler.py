import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_code(prompt):
    refined_prompt = f"Write clean and functional code for the following task. Only return the code block, no explanations.\n\nTask: {prompt}"
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(refined_prompt)
        return response.text.strip()
    except Exception as e:
        return f"# Error generating code: {e}"




