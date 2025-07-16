################################################################################
#
# Program: Rename A File
# 
# Description: Rename a file using the os module's rename() function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=KCn38p7xjFw
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import os 

# old and new file names
old_name = "file1.txt"
new_name = "new.txt"

# Attempt to rename the file.  The rename() function will throw suitable
# exceptions for different circumstances if it cannot succeed, which we can 
# handle, in addition to a catch all case.
try:
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'")
except FileNotFoundError:
    print(f"File '{old_name}' not found.")
except FileExistsError:
    print(f"A file named '{new_name}' already exists.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")