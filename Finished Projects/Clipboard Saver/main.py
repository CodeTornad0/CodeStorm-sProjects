"""Write everything the user copies into a file, so the user never loses what they copied."""


import pyperclip
import os
import time

FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
CLIPBOARD_PATH = f"{FOLDER_PATH}/clipboard.txt"


def main():
    """
    Continuously monitor the clipboard for changes, open the file if so,
    get the content from the clipboard, get the current time, and write
    the content copied with the time stamp.
    """

    while True:
        if pyperclip.waitForNewPaste():
            with open(CLIPBOARD_PATH, "a", encoding="utf-8") as file:
                # Get the new content from the clipboard
                user_copied_text = pyperclip.paste()
                # Get the hour:minute AM or PM
                current_clock_time = time.strftime("%l:%M %p")
                file.write(f"{user_copied_text} |END| {current_clock_time} \n")


if __name__ == "__main__":
    main()
