Host-Based Intrusion Detection System (HIDS)
============================================

A modular, beginner-friendly Python project that monitors key security telemetry on Windows systems. This HIDS agent captures keystrokes, clipboard activity, periodic screenshots, and process creation events, encrypting all log data for confidentiality and integrity. It includes a standalone decryption tool to securely review captured data.

---

Features
--------

- **Keystroke Monitoring:** Records every key press with timestamps, securely encrypted.
- **Clipboard Monitoring:** Detects and logs any changes in clipboard content.
- **Screenshot Capture:** Takes full-screen snapshots periodically, encrypted for privacy.
- **Process Monitoring:** Watches for new process creation events in real time.
- **Encrypted Logs:** All logs are symmetrically encrypted with Fernet to protect sensitive data.
- **Standalone Decryptor:** A separate script allows secure decryption and review of logs.
- **Modular Codebase:** Each monitoring component runs in its own thread for efficient performance.

---

Getting Started
---------------

### Prerequisites

- Python 3.7 or higher
- Windows operating system (for full functionality)
- Recommended: Run in a virtual environment

### Installation

1. Clone or download this repository.

2. Create and activate a Python virtual environment:

   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # Command Prompt
   venv\Scripts\activate.bat

3. Install dependencies:

   pip install -r requirements.txt

4. Generate an encryption key (only once):

   python keygen.py

   This creates `encryption.key`, which is critical to encrypt and decrypt logs. Keep it safe.

---

Running the HIDS Agent
----------------------

Start the integrated monitoring agent:

   python hids_agent.py

The agent will begin monitoring keystrokes, clipboard, processes, and screenshots, writing encrypted log files to the `logs/` directory.

---

Viewing Logs
------------

Use the standalone decryptor script to securely view logs:

   python decrypt_logs.py

Screenshots will be saved as PNG files in the current directory during decryption.

---

Project Structure
-----------------

hids_agent/
│
├── hids_agent.py            # Main integrated agent script
├── logger.py               # Encrypted logging utility
├── keystroke_monitor.py    # Keystroke capture module
├── clipboard_monitor.py    # Clipboard monitoring module
├── screenshot_monitor.py   # Periodic screenshot capture
├── process_monitor.py      # Process creation monitoring
├── decrypt_logs.py         # Standalone log decryption script
├── keygen.py               # Encryption key generation utility
├── requirements.txt        # Python dependency list
├── README.md               # This documentation
├── .gitignore              # Git ignore rules
└── logs/                   # Folder storing encrypted log files (gitignored)

---

Security and Ethical Considerations
-----------------------------------

- This project is for educational and portfolio purposes only.
- Use responsibly on systems where you have explicit permission.
- Encrypted logs contain sensitive user input; handle with care.
- Do not deploy on production or systems with sensitive data without proper authorization.

---

License
-------

This project is licensed under the MIT License.

---

Contact
-------

For questions or suggestions, please contact Aswin at aswindasm84@gmail.com.

Thank you for checking out this HIDS project.  
Happy coding! stay safe!
