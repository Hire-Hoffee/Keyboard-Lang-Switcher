import time
import pyperclip
from text_convert import get_current_layout, replace_text
from keyboard_shortcuts import copy, paste
import settings


def copy_paste():
    # Copy selected text to the clipboard
    copy()

    text = pyperclip.paste()

    if text.strip() == "":
        print("No text selected")
        return

    layout = get_current_layout()
    translated_text = replace_text(text, layout)
    pyperclip.copy(translated_text)

    # Simulate Ctrl+V press to paste
    paste()

    # Small delay before clearing the clipboard
    time.sleep(settings.CLEAR_CLIPBOARD_DELAY)
    # Clear the clipboard after pasting
    pyperclip.copy("")
