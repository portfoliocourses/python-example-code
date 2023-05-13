################################################################################
#
# Program: Delete A File
# 
# Description: Examples of deleting a file using the os module's remove() 
# function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=pArDll8HVh4  
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import os

# Will delete the file f1.txt in the current working directory
os.remove("f1.txt")

# If the file does not exist we'll get an error if we try to delete it so we 
# could use the os.path.exists() function to check if the file exists... the 
# function will return True if the file it's passed as an argument exists and 
# false otherwise.
if (os.path.exists("f1.txt")):
    os.remove("f1.txt")
else:
    print("File does not exist")

# Both exists() and remove() will accept a path to the file as an argument 
# as well... here we try to delete the file f2.txt in the subdirectory "subdir"
# of the current working directory.
if (os.path.exists("subdir/f2.txt")):
    os.remove("subdir/f2.txt")
else:
    print("File does not exist")