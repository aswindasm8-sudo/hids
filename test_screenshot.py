from cryptography.fernet import Fernet
import os

# Load key
key = open("encryption.key", "rb").read()
cipher = Fernet(key)

# Read first captured screenshot entry
with open("logs/screenshots.bin", "rb") as f:
    first_line = f.readline().strip()

decrypted = cipher.decrypt(first_line)

# Save as test.png to view
with open("test.png", "wb") as img_file:
    img_file.write(decrypted)

print("Decrypted screenshot saved as test.png")
