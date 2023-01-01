################################################################################
#
# Program: String isdigit() Method
# 
# Description: An example of using the string isdigit() method in Python. 
#
# YouTube Lesson: https://www.youtube.com/watch?v=MudyWmDC4oM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The isdigit() method will return true if a string contains only digit 
# characters and false otherwise.

# string contains only digits so isdigit() will return true
string = "123567890"
print( string.isdigit() )

# string contains a non-digit character 'a' so isdigit() will return false
string = "123a"
print( string.isdigit() )

# string contains a space character so isdigit() will return false
string = "123 "
print( string.isdigit() )

# period/dot '.' character used as a decimal separator is not considered a digit
# and so isdigit() will return false
string = "20.50"
print( string.isdigit() )

# roman numeral characters are not considered digits, so isdigit() will return
# false
string = "Ⅶ"
print( string.isdigit() )

# fraction characters are not considered digits, so isdigit() will return false
string = "½"
print( string.isdigit() )

# superscript and subscript digit characters are considered digits, so isdigit()
# will return true
string = "²₂"
print( string.isdigit() )