import time
from pynput import keyboard
from copy_paste import copy_paste
import settings

# Variables to track the state of double press
last_key = None
last_time = 0


def on_press(key):
    global last_key, last_time
    current_time = time.time()

    try:
        # Check if the key is correct
        if key == getattr(keyboard.Key, settings.DOUBLE_PRESS_KEY):
            # Check if the pressed key is the same as the previous one and if it was pressed within the double press interval
            if (
                key == last_key
                and (current_time - last_time) <= settings.DOUBLE_PRESS_INTERVAL
            ):
                copy_paste()

                # Сброс значений
                last_key = None
                last_time = 0
            else:
                # Update state for the next press
                last_key = key
                last_time = current_time
        else:
            # If the key is not correct, ignore it
            pass

    except Exception as e:
        print(f"Error: {e}")


def on_release(key):
    pass
