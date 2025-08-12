import psutil
import time
import logger
import threading

def start_process_monitor(cipher, interval=5):
    """
    Monitors new processes every `interval` seconds.
    Logs any new process starts with timestamp, encrypted and appended to logs/processes.bin.
    """

    # Capture the current known set of process IDs on startup
    known_pids = {p.pid for p in psutil.process_iter()}

    def monitor():
        nonlocal known_pids
        while True:
            current_pids = {p.pid for p in psutil.process_iter()}
            new_pids = current_pids - known_pids  # Find processes that started since last check

            for pid in new_pids:
                try:
                    proc = psutil.Process(pid)
                    proc_info = f"{pid}:{proc.name()}"
                    entry = logger.timestamped_bytes("PROC", proc_info.encode())
                    logger.encrypt_and_write(entry, "processes.bin", cipher)
                except psutil.NoSuchProcess:
                    # Process ended before we could log it
                    continue

            known_pids = current_pids
            time.sleep(interval)

    # Run the monitor loop in a daemon thread so it won't block program exit
    t = threading.Thread(target=monitor, daemon=True)
    t.start()
    return t
