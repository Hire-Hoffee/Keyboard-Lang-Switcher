import time
import pyperclip
from text_convert import get_current_layout, replace_text
from keyboard_shortcuts import (
    copy,
    paste,
    change_layout,
    copy_last_word,
)
import settings.settings as settings

get_clipboard_data = pyperclip.paste
set_to_clipboard = pyperclip.copy


def copy_paste():
    # Save the current clipboard data and clear it
    data = get_clipboard_data()
    set_to_clipboard("")

    # Copy the current selected text
    copy()

    default_text = get_clipboard_data()

    # If the clipboard is empty, copy the last typed word
    if default_text.strip() == "":
        copy_last_word()
        text = get_clipboard_data()
    else:
        text = default_text

    # If the copied text is still empty then return
    if text.strip() == "":
        return

    # Translate the text
    layout = get_current_layout()
    translated_text = replace_text(text, layout)
    set_to_clipboard(translated_text)

    # Paste text and change the keyboard layout
    paste()
    change_layout()

    # Set the clipboard data back to the original value
    time.sleep(settings.CLIPBOARD_DELAY)
    set_to_clipboard(data)
