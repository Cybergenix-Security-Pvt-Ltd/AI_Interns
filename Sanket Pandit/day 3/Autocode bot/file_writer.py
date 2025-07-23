import os
from datetime import datetime

def get_file_extension(language):
    return {
        "python": ".py",
        "javascript": ".js",
        "cpp": ".cpp",
        "c": ".c",
        "java": ".java",
    }.get(language.lower(), ".txt")

def write_code_to_file(code, language):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    extension = get_file_extension(language)
    filename = f"autocode_{timestamp}{extension}"
    filepath = os.path.join("logs", filename)
    os.makedirs("logs", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    with open(os.path.join("logs", "history.log"), "a", encoding="utf-8") as log:
        log.write(f"{timestamp} | {language} | {filename}\n")
    return filepath

