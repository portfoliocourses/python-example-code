################################################################################
#
# Program: Count The Number Of Lines In A File
# 
# Description: Example of how to count the number of lines in a file using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=qjrRf_pXWFQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# returns the number of lines in a file with the given filename
def count_lines(filename):
  
  # open the file with the given filename
  with open(filename) as file:
    
    # readlines() method returns a list containing each line of the file
    lines = file.readlines()
    
    # find the length of the list using len(), i.e. the # of lines in the file
    total_lines = len(lines)
    
    # return the number of lines
    return total_lines 

# use the count_lines() function to get the number of lines in the file
count = count_lines("file.txt")

# output the total number of lines in the file
print("Total:", count)