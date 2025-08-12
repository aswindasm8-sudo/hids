import os
from cryptography.fernet import Fernet

# Folders and files
LOGS_DIR = "logs"
KEY_FILE = "encryption.key"

def load_key():
    """Load the symmetric Fernet encryption key."""
    if not os.path.exists(KEY_FILE):
        print(f"[ERROR] Encryption key file not found: {KEY_FILE}")
        exit(1)
    with open(KEY_FILE, "rb") as f:
        return f.read()

def decrypt_file(filepath, cipher):
    """Decrypt each line (entry) from a given log file."""
    entries = []
    with open(filepath, "rb") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                decrypted = cipher.decrypt(line)
                entries.append(decrypted)
            except Exception as e:
                entries.append(f"[ERROR decrypting line {i}] {e}".encode())
    return entries

def save_image(img_bytes, count):
    """Save decrypted screenshot bytes as a PNG file."""
    filename = f"decrypted_screenshot_{count}.png"
    with open(filename, "wb") as img_f:
        img_f.write(img_bytes)
    return filename

def main():
    print("=" * 50)
    print("      HIDS LOG DECRYPTOR")
    print("=" * 50)

    # Show where we are looking
    logs_path = os.path.abspath(LOGS_DIR)
    print(f"[INFO] Looking for logs in: {logs_path}")

    # Check logs folder exists
    if not os.path.exists(LOGS_DIR):
        print("[ERROR] No 'logs' folder found. Run the HIDS agent first.")
        return

    # Load the encryption key
    try:
        key = load_key()
        cipher = Fernet(key)
    except Exception as e:
        print(f"[ERROR] Could not load key: {e}")
        return

    files = sorted(os.listdir(LOGS_DIR))
    if not files:
        print("[INFO] No log files found in logs/ folder.")
        return

    screenshot_counter = 0

    # Process each log file
    for log_file in files:
        log_path = os.path.join(LOGS_DIR, log_file)
        if not os.path.isfile(log_path):
            continue

        print(f"\n--- Decrypting {log_file} ---")
        entries = decrypt_file(log_path, cipher)

        if not entries:
            print(f"[INFO] {log_file} is empty.")
            continue

        for entry in entries:
            # Split into PREFIX, TIMESTAMP, DATA
            try:
                prefix, timestamp, rest = entry.split(b" ", 2)
                ts_str = timestamp.decode(errors="ignore")
            except ValueError:
                print(entry.decode(errors="ignore"))
                continue

            if prefix == b"KEY":
                print(f"[KEY]  {ts_str} - {rest.decode(errors='ignore')}")
            elif prefix == b"CLIP":
                print(f"[CLIP] {ts_str} - {rest.decode(errors='ignore')}")
            elif prefix == b"PROC":
                print(f"[PROC] {ts_str} - {rest.decode(errors='ignore')}")
            elif prefix == b"IMG":
                screenshot_counter += 1
                img_file = save_image(rest, screenshot_counter)
                print(f"[IMG]  {ts_str} - Screenshot saved as {img_file}")
            else:
                print(f"[UNKNOWN] {ts_str} - {rest[:30]}...")

    print("\n[INFO] Decryption complete.")
    if screenshot_counter:
        print(f"[INFO] {screenshot_counter} screenshots saved in current folder.")

if __name__ == "__main__":
    main()

