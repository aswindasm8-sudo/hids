# test_keys.py
from cryptography.fernet import Fernet
import keystroke_monitor
import time

# Load the same encryption key
key = open("encryption.key", "rb").read()
cipher = Fernet(key)

keystroke_monitor.start_keystroke_monitor(cipher)

print("Keystroke monitor running... Type some keys in this window.")
time.sleep(10)  # capture keystrokes for 10 seconds
print("Done. Check logs/keys.bin for encrypted entries.")
