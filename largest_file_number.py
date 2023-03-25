################################################################################
#
# Program: Find The Largest Number In A File
#
# Description: Find the largest number in a file usinh Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Z89BKMDJPGI
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The program assumes that the file has one number per line, for example:
#
# 12.44
# 80.56
# -45.6
# 23.45
# 90.23
# 12.66

# Prompt the user to enter the name of the file to open, store it into filename
filename = input("Filename: ")

# Open the file with the provided filename for reading, use the readline() 
# method of the file object to get a list of strings of all lines in the file.
with open(filename) as file:
    line_list = file.readlines()

# Use list comprehension to convert all strings in the file to float values
float_list = [float(n) for n in line_list]

# max() will return the largest float value in the list
largest = max(float_list)

# Output the largest value
print("Max:", largest)