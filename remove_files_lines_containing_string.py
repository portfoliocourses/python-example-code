################################################################################
#
# Program: Delete All Lines In A File That Contain A String
# 
# Description: Program to delete all lines in a file that contain a string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Wsejkkv_tPg 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user for the filename and the string text
filename = input("File: ")
text = input("Text: ")

# Open the file for reading.  Use the resulting file object's readlines() method
# to read all the lines of the file, the method will return all the lines of the
# file as strings in a list.  We then use a list comprehension to go through 
# each line and ONLY include the line in the filtered list if the string text is
# NOT in the line.  So all the lines that DO include this string will NOT be 
# included in this new filtered list.
with open(filename) as file:
    lines = file.readlines()
    filtered = [line for line in lines if text not in line]

# Open the file for writing with the "w" argument, which will cause the file to
# become blank until we write content to it.  Loop through the lines in the
# filtered list and write each line to the file.  Because we only write the 
# lines NOT containing the string back to the file, we have effectively deleted
# the lines that DO contain the string from the file.
with open(filename, "w") as file:
    for line in filtered:
        file.write(line)