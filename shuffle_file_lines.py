################################################################################
#
# Program: Shuffle The Lines Of A File
# 
# Description: Program to shuffle the lines of a file using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=rjty0sSrFZc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Used to randomize the order of the lines in a file...
import random 

# Prompt the user for the filename for which they want to shuffle the lines, 
# store the string entered into filename.
filename = input("Filename: ")

# Open the file with the given filename for reading, use the file object to 
# read the lines of the file.  The readlines() method will return the lines of
# the file stored as strings in a list, which we store into lines.
with open(filename) as file:
    lines = file.readlines()

# The shuffle function of the random module will randomly re-arrange the 
# strings stored in the random list, effectively randomly shuffling "the lines
# of the file".
random.shuffle(lines)

# Open the same file for writing (i.e. writing mode, where what we write to 
# the file will replace the existing content of the file).  We use the 
# writelines() method of the file object to write the lines of the file 
# BACK TO the file, but this time in their new shuffled order.
with open(filename, "w") as file:
    file.writelines(lines)