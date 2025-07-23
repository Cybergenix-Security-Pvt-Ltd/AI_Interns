import subprocess
import os
import platform

def open_in_editor(filepath, editor="vscode"):
    if editor.lower() == "vscode":
        try:
            subprocess.run(["code", filepath], shell=True, check=True)
        except Exception as e:
            print(f"Failed to open in VS Code: {e}")
    elif editor.lower() == "notepad":
        if platform.system() == "Windows":
            os.startfile(filepath)
        else:
            print("Notepad supported only on Windows.")

