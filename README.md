# cli-tg
A simple python script to upload your files from cli/ubuntu to telegram channel by using Pyrogram


How It Works

1. File Stability Check:
The function is_file_stable(file_path, wait_time=5) checks if the file size remains constant for 5 seconds. If the file size changes during this time, it skips the file (assuming it is still being downloaded or modified).


2. Upload Stable Files:
Only files confirmed as stable are uploaded to Telegram.


3. Automatic Deletion:
After successful upload, the script deletes the file from the folder.


4. Retry Mechanism:
Unstable files are skipped for now but will be checked again during the next scan (every 5 seconds).



Advantages

Prevents incomplete files from being uploaded or deleted prematurely.

Ensures smooth handling of files being actively downloaded or modified.
