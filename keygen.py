from cryptography.fernet import Fernet

# Generate a new Fernet key
key = Fernet.generate_key()

# Save the key to 'encryption.key'
with open("encryption.key", "wb") as f:
    f.write(key)

print("Key generated and saved to encryption.key")
print(f"Key (keep this secret!): {key.decode()}")
