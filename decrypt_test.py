from cryptography.fernet import Fernet

key = open("encryption.key", "rb").read()
cipher = Fernet(key)

with open("logs/clipboard.bin", "rb") as f:
    for line in f:
        print(cipher.decrypt(line).decode(errors="ignore"))
