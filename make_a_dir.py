################################################################################
#
# Program: Create A Directory
# 
# Description: Examples of making a directory using the built-in os module's
# mkdir() function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=hZ0GKf7HFo0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The mkdir() function is included in the os module.
import os

# Will create a new directory called new1 in the current working directory
os.mkdir("new1")

# We could supply an absolute/full path instead, e.g. create a directory called
# new2 in the directory /Users/kevinbrowne/video
os.mkdir("/Users/kevinbrowne/video/new2")

# If the directory already exists the function will raise a FileExistsError 
# exception, which we could catch using try-except to handle this case.
try:
    os.mkdir("/Users/kevinbrowne/video/new2")
except:
    print("make dir failed")