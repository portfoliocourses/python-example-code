################################################################################
#
# Program: String isdecimal() Method
#
# Description: Examples of using the isdecimal() String method in Python to 
# check if a string consists of only decimal characters (effectively, only the 
# characters from 0-9).
#
# YouTube Lesson: https://www.youtube.com/watch?v=WjC0g9pXopk 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The isdecimal() method will return true if the string  consists of only 
# decimal characters from 0-9.
string = "012346789 "
print( string.isdecimal() )

# A . character does not count as a decimal character and so the method will 
# return false below.
string = "0123.46789 "
print( string.isdecimal() )

# Letter characters do not count as decimal characters and so the method will 
# return false below.
string = "0123a46789 "
print( string.isdecimal() )

# Space characters do not count as decimal characters and so the method will 
# return false below.
string = "012346789 "
print( string.isdecimal() )

# Decimal characters from other types of numerals included in Unicode will be 
# recogonized by isdecimal() so the below string made up of only the Bengali 
# numerals will result in the method returning true.
string = "০১২৩৪৫৬৭৮৯"
print( string.isdecimal() )

# The method has a strict interpretation of a decimal... so a superscript 2 
# character is not considered a decimal and the below call to isdecimal() 
# will return false.
string = "²"
print( string.isdecimal() )

# Other methods like isdigit() and isnumeric() will return true though!
string = "²"
print( string.isdigit())