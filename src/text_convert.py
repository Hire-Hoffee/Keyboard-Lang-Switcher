import subprocess
import ast
from pathlib import Path
import json
import settings

# Dictionaries for text transformation depending on the keyboard layout
json_file = Path(settings.DICTIONARY_PATH)

first_to_second = json.loads(json_file.read_text())
second_to_first = {v: k for k, v in first_to_second.items()}


# Function for text transformation depending on the keyboard layout
def replace_text(text, layout):
    if layout == settings.LANGUAGES[0]:
        return "".join(first_to_second.get(char, char) for char in text)
    elif layout == settings.LANGUAGES[1]:
        return "".join(second_to_first.get(char, char) for char in text)
    else:
        return text


# Function to get the current keyboard layout
def get_current_layout():
    result = subprocess.run(
        ["gsettings", "get", "org.gnome.desktop.input-sources", "mru-sources"],
        stdout=subprocess.PIPE,
        text=True,
    )
    parsed_list = ast.literal_eval(result.stdout)

    return parsed_list[0][1]
