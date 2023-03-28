################################################################################
#
# Program: Find The Smallest Number In A File
#
# Description: Find the smallest number in a file using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=YWnaIXxaJ-k 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The program assumes that the file has one number per line, for example:
#
# 12.44
# 80.56
# 10.95
# 23.45
# 90.23
# 12.66

# Prompt the user to enter the name of the file to open, store it into filename
filename = input("Filename: ")

# Open the file with the provided filename for reading, use the readline() 
# method of the file object to get a list of strings of all lines in the file.
with open(filename) as file:
  lines_list = file.readlines()

# Use list comprehension to convert all strings in the file to float values
float_list = [float(n) for n in lines_list]

# min() will return the smallest float value in the list
smallest = min(float_list)

# Output the smallest value
print("Min:", smallest)