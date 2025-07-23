import re

def detect_language_from_prompt(prompt):
    prompt = prompt.lower()
    if re.search(r"python", prompt):
        return "python"
    elif re.search(r"javascript", prompt):
        return "javascript"
    elif re.search(r"c\+\+|cpp", prompt):
        return "cpp"
    elif re.search(r"java(?!script)", prompt):
        return "java"
    elif re.search(r"\bc program\b", prompt):
        return "c"
    return "text"
