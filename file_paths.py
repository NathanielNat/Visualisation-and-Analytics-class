import os

# list all directories in current folder
# Using scandir
# with os.scandir('data_files/') as entries:
#     for entry in entries:
#         print(entry.name)

## using listdir
# entries = os.listdir('data_files/')
# for entry in entries:
#     print(entry)
# using pathlin
# from pathlib import Path

# entries = Path('data_files/')
# for entry in entries.iterdir():
#     print(entry.name)

# Using pathlib.Path() or os.scandir() instead of listdir() is the preferred way of getting a directory listing, especially when you’re working with code that needs the file type and file attribute information. pathlib.Path() offers much of the file and path handling functionality found in os and shutil, and it’s methods are more efficient than some found in these modules. 