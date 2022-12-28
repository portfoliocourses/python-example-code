################################################################################
#
# Program: Escape Character Examples
#
# Description: Examples of escape characters (i.e. escape sequences) in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=4rBPrJfF-GM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Escape characters allow us to represent and output special characters or 
# output characters in special ways.  Check out the effect of these characters 
# below...

# \n - newline character will start additional output on the next line
print("Line 1\nLine 2")

# \t - tab character
print("Before Tab\tAfter")

# \b - backspace character will move cursor back one space, causing overwriting
print("Some text\b\b\b in a string")

# \\ - \ allows us to output a backspace character instead of things like tab!
print("lions\\tigers\\bears")

# \r - carriage return returns cursor to the start of the line, causing 
# overwriting of text similar to backspace
print("Writing old text\rNew text")

# \" - " allow us to output a double quote character despite it being used as 
# the character to create a string
print("A \" inside a string")

# \' - ' allows us to output a single quote character despite it being used as
# the character to create a string (Python allows us to create strings with 
# both single and double quote characters).
print('A \' inside a string')

# Characters in Python and in computing in general are represented with numbers
# according to some encoding (mapping of numbers to characters), for example 
# in the ASCII and UTF-8 encodings 'A' is represented with 65.  We would call
# 65 a base 10 number, 10 digits are used to represent base 10 numbers.  There
# are also octal numbers where 8 digits are used to represent numbers, and 
# hexadecimal numbers where 16 digits are used to represent numbers.  The 
# below two escape sequences allow us to output the character associated with 
# a number, where the number is either an octal number or hexadecimal number.
#
# 'A' - 65 where 65 is a base 10 number
#
# 65 in base 10 is 101 in octal
#
# 65 in base 10 is 41 in hexadecimal
#

# \ooo - octal number
print("char: \101")

# \xhh - hexadecimal number
print("char: \x41")

# \f - form feed character traditionally used to represent 'page breaks' that 
# instruct a printer to begin printing on a new page, but is also sometimes used
# in source code files to mark page breaks or sections of code. 
print("Page 1\fPage 2")