import os
from datetime import datetime

def encrypt_and_write(data: bytes, filename: str, cipher):
    """
    Encrypt `data` bytes using the Fernet cipher and append to the log file.

    Each encrypted entry ends with a newline for easy parsing.
    A folder 'logs' is created if not existing to hold all log files.
    """
    os.makedirs("logs", exist_ok=True)
    token = cipher.encrypt(data)
    with open(os.path.join("logs", filename), "ab") as f:
        f.write(token + b"\n")

def timestamped_bytes(prefix: str, payload: bytes) -> bytes:
    """
    Return a bytes string with ISO8601 UTC timestamp and prefix prepended to payload.

    Format: b"{prefix} {timestamp} {payload}"
    Example: b"KEY 2025-08-12T05:24:00Z pressed a"
    """
    ts = datetime.utcnow().isoformat().encode()  # UTC time for consistency
    return prefix.encode() + b" " + ts + b" " + payload
