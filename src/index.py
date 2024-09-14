from pynput import keyboard
from keyboard_listener import on_press, on_release

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
