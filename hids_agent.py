from cryptography.fernet import Fernet
import keystroke_monitor
import clipboard_monitor
import screenshot_monitor
import process_monitor
import time

def main():
    # 1. Load encryption key
    with open("encryption.key", "rb") as f:
        cipher = Fernet(f.read())

    print("[HIDS] Starting all monitors...")

    # 2. Start each monitor
    keystroke_monitor.start_keystroke_monitor(cipher)
    clipboard_monitor.start_clipboard_monitor(cipher, interval=1)
    screenshot_monitor.start_screenshot_monitor(cipher, interval=60)  # every 60s
    process_monitor.start_process_monitor(cipher, interval=5)         # every 5s

    print("[HIDS] All monitors active. Logs are encrypted in the 'logs' folder.")
    print("[HIDS] Press Ctrl+C to stop.")

    # 3. Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[HIDS] Stopped by user.")

if __name__ == "__main__":
    main()
