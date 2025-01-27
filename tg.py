import os
import time
from pyrogram import Client

# Replace with your API credentials
API_ID = 2822198  # Replace with your Telegram API ID
API_HASH = "abcdxyzzz"  # Replace with your Telegram API Hash
BOT_TOKEN = "7466220003:AAFDFPQ3HHlcCDanOiE0cLES7Z6bTrY"
CHAT_ID = -100180900922  # Replace with your Telegram chat ID (group or channel)

# Default folder path for uploads
DEFAULT_PATH = "/home/vinesh4540/gogoanime-downloader/CommandLineUI/naruto"

def is_file_stable(file_path, wait_time=10):
    """
    Checks if a file is stable (not being modified).
    Args:
        file_path (str): Path of the file to check.
        wait_time (int): Duration to wait (in seconds) to confirm stability.
    Returns:
        bool: True if the file is stable, False otherwise.
    """
    try:
        initial_size = os.path.getsize(file_path)
        time.sleep(wait_time)
        current_size = os.path.getsize(file_path)
        return initial_size == current_size
    except Exception as e:
        print(f"Error checking file stability: {e}")
        return False

def send_files_in_folder(folder_path):
    """Sends all stable files in a folder to a Telegram chat using Pyrogram."""
    try:
        # Create a Pyrogram Client
        with Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) as app:
            if os.path.isdir(folder_path):
                # Iterate through all files in the folder
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):  # Only process files, skip directories
                        if is_file_stable(file_path):  # Check if the file is stable
                            try:
                                app.send_document(chat_id=CHAT_ID, document=file_path)
                                print(f"File '{file_name}' sent successfully!")
                                os.remove(file_path)  # Delete file after sending
                                print(f"File '{file_name}' deleted after upload.")
                            except Exception as upload_error:
                                print(f"Error uploading '{file_name}': {upload_error}")
                        else:
                            print(f"File '{file_name}' is still being modified. Skipping for now.")
            else:
                print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = DEFAULT_PATH  # Use the default path
    print(f"Monitoring folder: {folder_path}")

    # Infinite loop to monitor the folder every 10 seconds
    while True:
        send_files_in_folder(folder_path)
        time.sleep(10)  # Wait 10 seconds before scanning again
