################################################################################
#
# Program: String splitlines() Method
# 
# Description: Examples of using the splitlines() String method in Python to 
# split a string into a list made up of the lines in the string.
#
# YouTube Lesson: https://www.youtube.com/watch?v=UNL1GQ-QZQA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# The splitlines() method will return a list containing the lines in the string
# for which it was called.  So for example the below string has 4 lines, 
# separated by the line boundaries '\n' (the newline character).  So the method
# will return the 4 lines in a string.

text = "line 1\nline 2\nline 3\nline 4"

lines = text.splitlines()

print(lines)

for line in lines:
  print(line)


# The splitlines() method has an optional keepends parameter that is by default 
# set to False.  If we supply True as an argument keepends will be set to True, 
# and as a result the line boundaries will remain in the split strings.  So 
# we will have "line 1\n" for example as the first string in the list of strings
# instead of only "line 1" as in the above example.

text = "line 1\nline 2\nline 3\nline 4"

lines = text.splitlines(True)

print(lines)

for line in lines:
  print(line)  


# There are other line boundaries along which the string will be split, such as 
# carriage return \r and form feed \f.  A complete list is found at the bottom 
# of this file.

text = "line 1\nline 2\rline 3\fline 4"

lines = text.splitlines(True)

print(lines)

for line in lines:
  print(line)  


# Notably when the method is called with an empty string it will return an 
# empty list.

text = ""

lines = text.splitlines(True)

print(lines)

for line in lines:
  print(line)  


# Also notably if the method is called with a string containing only a single 
# line boundary and with endswith set to False, it will return a list containing
# a single empty string.

text = "\n"

lines = text.splitlines(False)

print(lines)

for line in lines:
  print(line)  


#  Line Boundaries
#  ---------------
#
#  Representation  Description
#
#  \n              Line Feed
#  \r              Carriage Return
#  \r\n            Carriage Return + Line Feed
#  \v or \x0b      Line Tabulation
#  \f or \x0c      Form Feed
#  \x1c            File Separator
#  \x1d            Group Separator
#  \x1e            Record Separator
#  \x85            Next Line (C1 Control Code)
#  \u2028          Line Separator
#  \u2029          Paragraph Separator
#
#
#  See official documentation: 
#    https://docs.python.org/3/library/stdtypes.html