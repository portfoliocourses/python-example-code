################################################################################
#
# Program: String isprintable() Method
# 
# Description: Examples of using the isprintable() method in Python to check if 
# all of the characters in a string are printable.
#
# YouTube Lesson: https://www.youtube.com/watch?v=MLTkkeiHIdM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Letters, digits, the space character, symbols and punctuation marks are all 
# considered printable characters, and so the method will return True for the 
# the below string as ALL characters in the string are printable.
string = "ABCabc123 $@!"
print( string )
print( string.isprintable() )

# If even one character in the string is not printable the method will return 
# False. Formatting characters such as newline and table are not considered 
# printable so the below string with the newline character \n will cause the 
# method to return False. 
string = "ABCabc123 $@!\n"
print( string )
print( string.isprintable() )

# Other characters are considered non-printable, \x18 is the 'cancel character',
# another non-printable character and so as a result the below call to the 
# method will return False.
string = "ABCabc123 $@!\x18"
print( string )
print( string.isprintable() )