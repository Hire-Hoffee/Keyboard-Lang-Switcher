from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()  # Create a keyboard controller


def copy():
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press("c")
    keyboard_controller.release("c")
    keyboard_controller.release(keyboard.Key.ctrl)


def paste():
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press("v")
    keyboard_controller.release("v")
    keyboard_controller.release(keyboard.Key.ctrl)
