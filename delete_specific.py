################################################################################
#
# Program: Delete A Specific Line From A File
# 
# Description: Example of how to delete a specific line from a file with Python.
# In this solution we read all of the lines of the file into a list, delete 
# the line/element from the list that we want to delete, then write the 
# remaining lines/elements back to the file.  There are other ways to solve 
# this problem but this is a nice beginner-friendly way!
#
# YouTube Lesson: https://www.youtube.com/watch?v=t6rIQlwDnpQ  
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Deletes the line with at line_number from the file with the given filename
def delete_line(filename, line_number):
  
  # opens the file, reads and stores each line into a list
  with open(filename) as file:
    lines = file.readlines()
  
  # if the line number is in the file, we can delete it
  if (line_number <= len(lines)):
  
    # delete the line from the list, which will be at line_number - 1 because 
    # lists are zero-indexed in Python
    del lines[line_number - 1]
    
    # open the file for writing with "w" which will make the file blank
    with open(filename, "w") as file:

      # write as the new content of the file, the remaining lines in the list
      for line in lines:
        file.write(line)
  
  # if the line number exceeds the length of the file, output an error message
  else:
    
    # inform the user the line is not in the file, and how many lines there is
    print("Line", line_number, "not in file.")
    print("File has", len(lines), "lines.")


# prompt the user for the filename and line number
delete_filename = input("File: ")
delete_line_number = int(input("Line: "))

# call the delete_line function to delete the line at that line number from 
# the file with that filename
delete_line(delete_filename, delete_line_number)