################################################################################
#
# Program: Replace A Specific Line In A File
# 
# Description: Example of how to replace a specific line in a file with Python.
# In this solution we read all of the lines of the file into a list, replace 
# the line/element in the list with the replacement text, then write the 
# list lines/elements back to the file.  There are other ways to solve this 
# problem but this is a nice beginner-friendly way!
#
# YouTube Lesson: https://www.youtube.com/watch?v=6v1bVWI8nl8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Replace the line at line_number in the file with the provided filename with 
# the text in the string text
def replace_line(filename, line_number, text):
  
  # Open the file and read all the lines from the file into a list 'lines'
  with open(filename) as file:
    lines = file.readlines()
  
  # if the line number is in the file, we can replace it successfully
  if (line_number <= len(lines)):
    
    # Replace the associated line in the list with the replacement text 
    # (followed by a newline \n to end the line), we need to use line_number - 1
    # as the index because lists are zero-indexed in Python.
    lines[line_number - 1] = text + "\n"
    
    # Open the file in 'writing mode' using the 2nd argument "w", this means 
    # that the file will be made blank, and any new text we write to the file 
    # will become the new file contents.
    with open(filename, "w") as file:

      # Loop through the list of lines, write each of them to the file
      for line in lines:
        file.write(line)
  
  # otherwise if the line number is past the length of the file, we can't 
  # replace the line so output an error message instead
  else:
  
    # Output the line number that was requested to be replaced and the number
    # of lines the file actually has to inform the user
    print("Line", line_number, "not in file.")
    print("File has", len(lines), "lines.")

# Prompt the user for the filename, line number and replacement text
filename = input("File: ")
line_number = int(input("Line: "))
text = input("Text: ")

# Call the replace_line() function to replace the text at the line number 
# 'line_number' in the file with the filename 'filename' with the replacement 
# text 'text'.
replace_line(filename, line_number, text)