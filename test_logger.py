# test_logger.py
from cryptography.fernet import Fernet
import logger

key = open("encryption.key", "rb").read()
cipher = Fernet(key)

data = logger.timestamped_bytes("TEST", b"This is a test log entry.")
logger.encrypt_and_write(data, "test.log", cipher)

print("Encrypted test entry written to logs/test.log")
