################################################################################
#
# Program: Append Text To A File
# 
# Description: Example of appending text to the end of a file using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=DveYpz8hU1U 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user for the file to append text to and store entered filename
# into filename
filename = input("File: ")

# Prompt the user for the text to append to the file and store the entered text
# into text
text = input("Text: ")

# Open the file with the given filename in APPEND mode due to using the second
# argument "a", then use the file object's write method to append the text 
# to the file.
with open(filename, "a") as file:
    file.write(text)