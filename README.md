# Keyboard Layout Text Converter for Linux

This Python script allows you to quickly convert the keyboard layout of selected text by double-pressing the Shift key. For example, if you have text typed in Russian and you need to quickly convert it to English, you can select the text and double-press Shift.

(You need to use GNOME environment for this script to work)

## Features

- Converts text between two specified keyboard layouts.
- Uses a customizable dictionary for accurate character mapping.
- Supports customizable double press interval and hotkey.
- Clears the clipboard after pasting the converted text.

## Requirements

- Python 3
- `pynput` library
- `pyperclip` library

You can install the required libraries using pip:

- ((Optional) Create and activate virtual environment with `python3 -m venv venv` and `source venv/bin/activate` commands)

```bash
pip install pynput pyperclip
```

## Installation

1. Clone the repository or download the source code.
2. If you want, update the `settings.py` file with your desired settings:
   - `DOUBLE_PRESS_INTERVAL`: Maximum time between presses for a double press (in seconds).
   - `DOUBLE_PRESS_KEY`: Key used for triggering the conversion (e.g., "shift").
   - `CLIPBOARD_DELAY`: Delay before manipulating with the clipboard (in seconds).
   - `LANGUAGES`: List of supported keyboard layouts (e.g., ["us", "ru"]).
   - `DICTIONARY_PATH`: Path to the JSON file containing the character mapping dictionary.
   - `KEYBOARD_SHORTCUTS`
     - `COPY_KEYS`: Shortcut for copying on your keyboard.
     - `PASTE_KEYS`: Shortcut for pasting on your keyboard.
     - `CHANGE_LAYOUT_KEYS`: Shortcut for changing language on your keyboard.
     - `COPY_LAST_WORD_KEYS`: Shortcut to select the last typed word on your keyboard.
3. If you want, update a JSON file named `dictionary.json` in the project root directory. This file should contain a dictionary mapping characters between the two keyboard layouts.

## Usage

1. Run the `python3 src/index.py` command (you can run the script on the background by `nohup python3 src/index.py`).
2. Select the text you want to convert (if not selected, the last typed word will be converted).
3. Double-press the `Shift` key (or your configured hotkey).
4. The converted text will be pasted in place of the selected text.

- P.S. If you use virtual environment and script do not run, you can try this command `./venv/bin/python src/index.py`
- P.P.S. Maybe you need to install additional apt packages (check your terminal)

## How it Works

The script uses the `pynput` library to listen for keyboard events. When a double press of the specified key is detected, it copies the selected text to the clipboard, converts it using the character mapping dictionary, and pastes the converted text back. The `pyperclip` library is used for clipboard operations.

## Customization

You can customize the script's behavior by modifying the settings in the `settings.py` file and the character mapping dictionary in the `dictionary.json` file.
