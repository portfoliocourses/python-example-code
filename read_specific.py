################################################################################
#
# Program: Read A Specific Line From A File
# 
# Description: Read a specific line from a file (i.e. by line number) using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ZLCZkMk69y0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prints the line with the line number 'lnum' from the file with the filename 
# 'fname'.  Prints error messages if an exception occurs when reading the file, 
# or if the line number requested exceeds the number of lines in the file.
def read_line(fname, lnum):
  
  # attempt to open and read the lines of the file
  try:

    # open the file in reading mode
    file = open(fname, "r")

    # .readlines() returns a list of strings of each line in the file
    lines = file.readlines()

    # close the file as we have all the information we need
    file.close()

  # if an except occurs when attempting to read from the file, print an error
  # message  and terminate the function
  except:
    print("Error reading file.")
    return 
  
  # find the total number of lines in the file
  total_lines = len(lines)

  # if the line number requested is greater than the total number of lines, 
  # output an error message
  if (lnum > total_lines):

    # inform the user how many lines are in the file
    print(str(total_lines) + " file lines.")

    # reminder the user which line they requested so they can see it is beyond 
    # the number of lines in the file
    print("Can't read line " + str(lnum) + "!")
  
  # otherwise if we're able to print out the line, print it out
  else:

    # extract the line from the lines list, we subtract 1 from the line number 
    # because lists in Python are zero-indexed, and we use .rstrip('\n') to 
    # remove the trailing newline from the file (if there is one)
    line = lines[lnum - 1].rstrip('\n')

    # output the line
    print(line)

# use the function with a file called file.xt
read_line("file.txt", 1)

# we could also prompt the user for a filename and line number
filename = input("File: ")
line_number = int(input("Line: "))

# we could then call the function with these values the user provides
read_line(filename, line_number)