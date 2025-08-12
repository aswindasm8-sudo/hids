from cryptography.fernet import Fernet
import process_monitor
import time

# Load encryption key
key = open("encryption.key", "rb").read()
cipher = Fernet(key)

# Start process monitor with 5-second interval
process_monitor.start_process_monitor(cipher, interval=5)

print("Process monitor running for 20 seconds... Launch new apps to generate log entries.")
time.sleep(20)
print("Finished. Check logs/processes.bin for encrypted process logs.")
