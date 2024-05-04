################################################################################
#
# Program: Count The Occurrences Of A String In A File
#
# Description: Program to count the occurrences of a string in a file using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=QqCmA_T62Mc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user for the filename of the file to open and the text string to
# count the occurrences of in that file
filename = input("Filename: ")
text = input("Text: ")

# Open the file with the provided filename for read access
with open(filename) as file:

    # Read all the contents of the file, store them into contents
    contents = file.read()

    # Count the occurrences of the string text in the file contents
    text_count = contents.count(text)

    # Output the occurrences of the string in the file
    print("Count:", text_count)