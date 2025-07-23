from gpt_handler import generate_code
from file_writer import write_code_to_file
from launcher import open_in_editor
from utils import detect_language_from_prompt

def main():
    prompt = input("\U0001F4DD Enter your coding task:\n> ")

    print("\n⏳ Generating code...")
    code = generate_code(prompt)

    language = detect_language_from_prompt(prompt)
    filepath = write_code_to_file(code, language)

    print(f"✅ Code written to: {filepath}")

    editor_choice = input("Open file in (1) VS Code or (2) Notepad? [1/2]: ").strip()
    editor = "vscode" if editor_choice == "1" else "notepad"
    open_in_editor(filepath, editor)

if __name__ == "__main__":
    main()


