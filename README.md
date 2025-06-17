# 🛡️ Python Keylogger using pynput

This project is a **simple keylogger** built with Python and the [`pynput`](https://pypi.org/project/pynput/) library. It captures and logs all keystrokes to a local file (`keylog.txt`) along with timestamps. The logger runs silently in the background using threading and keyboard event listeners.

> ⚠️ **Disclaimer**: This tool is created strictly for **educational** and **authorized** use only. Do not use it on systems you don't own or without explicit consent. Unauthorized keylogging is illegal and unethical.

---

## 🚀 Features

- 🧠 Captures all keypress events.
- 🕒 Timestamps each keystroke.
- 🧵 Runs in the background using threads.
- 💾 Logs stored in a local file (`keylog.txt`).
- ✅ Works on Windows, Linux, and macOS (with Python & pynput installed).

---

## 📂 Project Structure

keylogger/
│
├── keylogger.py # Main script to start the keylogger
├── keylog.txt # Output log file (generated after running)
└── README.md # Project documentation

yaml

---

## ⚙️ Requirements

- Python 3.6+
- `pynput` library

Install dependencies:

```bash
pip install pynput
🧪 How It Works
A keyboard listener is created using pynput.keyboard.Listener.

Each keypress triggers the process_key_strike() function.

Regular keys, spaces, enters, and special keys are logged differently.

All logs are written to keylog.txt with a timestamp via the logging module.

The listener runs on a separate daemon thread, so it works in the background.


📁 Sample Output (keylog.txt)
yaml
Copy
Edit
2025-06-17 09:34:20,501 - h
2025-06-17 09:34:20,900 - e
2025-06-17 09:34:21,210 - l
2025-06-17 09:34:21,455 - l
2025-06-17 09:34:21,722 - o
2025-06-17 09:34:21,997 -  
2025-06-17 09:34:22,250 - w
2025-06-17 09:34:22,490 - o
2025-06-17 09:34:22,711 - r
2025-06-17 09:34:22,950 - l
2025-06-17 09:34:23,210 - d
