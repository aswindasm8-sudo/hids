from cryptography.fernet import Fernet
import clipboard_monitor
import time

# Load encryption key
key = open("encryption.key", "rb").read()
cipher = Fernet(key)

# Start clipboard monitoring
clipboard_monitor.start_clipboard_monitor(cipher)

print("Clipboard monitor running...")
print("Copy some text (CTRL+C) from anywhere, then come back here.")
time.sleep(15)  # wait and log a few changes
print("Finished test. Check logs/clipboard.bin for encrypted entries.")
