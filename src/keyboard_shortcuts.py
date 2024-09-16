from pynput import keyboard
from pynput.keyboard import Controller

keyboard_controller = Controller()


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


def change_layout():
    keyboard_controller.press(keyboard.Key.cmd)
    keyboard_controller.press(keyboard.Key.space)
    keyboard_controller.release(keyboard.Key.space)
    keyboard_controller.release(keyboard.Key.cmd)


def copy_last_word():
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press(keyboard.Key.shift_r)
    keyboard_controller.press(keyboard.Key.left)
    keyboard_controller.release(keyboard.Key.left)
    keyboard_controller.release(keyboard.Key.shift_r)
    keyboard_controller.release(keyboard.Key.ctrl)

    copy()
