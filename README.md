# Keyboard Layout Text Converter for Linux

This Python script allows you to quickly convert the keyboard layout of selected text by double-pressing the Shift key. For example, if you have text typed in Russian and you need to quickly convert it to English, you can select the text and double-press Shift.

(You need to use GNOME environment for this script to work)

## Features

- Converts text between two specified keyboard layouts.
- Uses a customizable dictionary for accurate character mapping.
- Supports customizable double press interval and hotkey.
- Clears the clipboard after pasting the converted text.

## Installation

1. Clone the repository or download the source code.
2. (Optional: Create and activate virtual environment with `python3 -m venv venv` and `source venv/bin/activate` commands)
3. Install the required libraries using pip `pip install -r requirements.txt`.
4. Optional: update the `src/settings/settings.py` file with your desired settings.
5. Optional: update a file `src/settings/dictionary.py` with your language. This file should contain a dictionary mapping characters between the two keyboard layouts.

## Usage

1. Run the `python3 src/index.py` command (you can run the script on the background by `nohup python3 src/index.py &`).
2. Select the text you want to convert (if not selected, the last typed word will be converted).
3. Double-press the `Shift` key (or your configured hotkey).
4. The converted text will be pasted in place of the selected text.

## How it Works

The script uses the `pynput` library to listen for keyboard events. When a double press of the specified key is detected, it copies the selected text to the clipboard, converts it using the character mapping dictionary, and pastes the converted text back. The `pyperclip` library is used for clipboard operations.

## Additionally

- If you use virtual environment and script do not run, you can try this command `./venv/bin/python src/index.py`.
- Maybe you need to install additional apt packages (check your terminal).
- You can create standalone executable with `pyinstaller -F -n=KeyboardLangSwitcher src/index.py` command. File will be located on dist directory.

## Systemctl service

You can create systemctl service to run this script on the background forever.

1. Create `keyboard-lang-switch.service` in `~/.config/systemd/user/` directory
2. Add this code to file with your path to execute script or standalone file

```
[Unit]
Description=Keyboard language switcher

[Service]
ExecStart=/bin/bash -c "<path to executable>"

[Install]
WantedBy=multi-user.target
```

3. Enable the service to start automatically when you log in `sudo systemctl --user enable keyboard-lang-switch.service`.
4. Start the service `sudo systemctl --user start keyboard-lang-switch.service`.
5. Verify that the service is running `sudo systemctl --user status keyboard-lang-switch.service`.
