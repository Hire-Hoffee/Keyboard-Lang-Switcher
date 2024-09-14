import time
from pynput import keyboard
import pyperclip
from pynput.keyboard import Controller
from text_convert import get_current_layout, replace_text
import settings

keyboard_controller = Controller()  # Create a keyboard controller


def copy_paste():
    # Copy selected text to the clipboard
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press("c")
    keyboard_controller.release("c")
    keyboard_controller.release(keyboard.Key.ctrl)

    text = pyperclip.paste()
    layout = get_current_layout()

    translated_text = replace_text(text, layout)
    pyperclip.copy(translated_text)

    # Simulate Ctrl+V press to paste
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press("v")
    keyboard_controller.release("v")
    keyboard_controller.release(keyboard.Key.ctrl)

    # Small delay before clearing the clipboard
    time.sleep(settings.CLEAR_CLIPBOARD_DELAY)
    # Clear the clipboard after pasting
    pyperclip.copy("")
