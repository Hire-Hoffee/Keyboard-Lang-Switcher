from pynput import keyboard
from pynput.keyboard import Controller
import settings

keyboard_controller = Controller()


# Press and release keys based on configuration
def press_keys(keys):
    for key in keys:
        if hasattr(keyboard.Key, key):
            key_to_press = getattr(keyboard.Key, key)
            keyboard_controller.press(key_to_press)
        else:
            keyboard_controller.press(key)

    for key in reversed(keys):
        if hasattr(keyboard.Key, key):
            key_to_press = getattr(keyboard.Key, key)
            keyboard_controller.release(key_to_press)
        else:
            keyboard_controller.release(key)


# Action functions
def copy():
    press_keys(settings.COPY_KEYS)


def paste():
    press_keys(settings.PASTE_KEYS)


def change_layout():
    press_keys(settings.CHANGE_LAYOUT_KEYS)


def copy_last_word():
    press_keys(settings.COPY_LAST_WORD_KEYS)
    press_keys(settings.COPY_KEYS)
