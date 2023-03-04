################################################################################
#
# Program: Find First And Last Substring Occurrences Using: find()  rfind() 
#                                                           index() rindex()
# 
# Description: Examples of finding the first and last occurrences of a character
# or a substring in a string using the string methods find() rfind() index() and
# rindex() in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=AYpccxEWlBE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The characters in a string are each located at an index 0, 1, 2, ...
#
#  0123456789...
# "To be or not to be"
# 
# The find() method returns the index of the first occurrence of a substring 
# in a string.

# find() will return 3 because the first occurrence of "be" in the string is 
# at the index 3
string = "To be or not to be"
index = string.find("be")
print(index)

# We can find the first occurrence of a character in a string by passing find 
# the string made up of only that character.  In this case the first occurrence
# of 'o' is at the index 1.
string = "To be or not to be"
index = string.find("o")
print(index)

# If the character or substring cannot be found at all in the string, then 
# find() will return -1.  There is no 'X' character in the string so below 
# find() will return -1.
string = "To be or not to be"
index = string.find("X")
print(index)

# There is no substring "whatever" in the string so find() will return -1.
string = "To be or not to be"
index = string.find("whatever")
print(index)

# We can pass an optional additional start index argument, and the search for 
# the substring will then begin from that index onwards until the end of the 
# string.  So normally the first occurrence of 'o' would be at the index 1 
# but here we get the index 6 because we are searching for 'o' from the index 
# 4 onwards.
string = "To be or not to be"
index = string.find("o", 4)
print(index)

# We can also pass an optional additional end argument which specifies where 
# to stop searching for the substring.  So below the substring "be" will be 
# found at the index 3 in between the indexes 3 and 5.  The end index is not 
# included in the range.
string = "To be or not to be"
index = string.find("be", 2, 5)
print(index)

# Because the end index is not included in the range, if we search for the 
# string "be" with start index 2 and end index 4, we'll get back -1, because 
# the only indexes search will be 2-3, not 4, and so the substring "be" is 
# not found within that range.
#
#           ** 
#         0123456789...
string = "To be or not to be"
index = string.find("be", 2, 4)
print(index)

# The index() method behaves exactly like find() except it will raise a
# ValueError exception if it cannot find the substring in the string.  So 
# below it will return 9 because the substring "not" first occurs at the 
# index 9.
string = "To be or not to be"
index = string.index("not")
print(index)

# We can also uses the start and end index arguments with index(), so the below
# will result in the index 6 because the first occurrence of 'o' between the 
# indexes 3 and 9 is at the index 6.
string = "To be or not to be"
index = string.index("o", 3, 9)
print(index)

# But if the substring cannot be found in the string then index() will raise a
# ValueError except.  For example if we uncomment the code below there is no 
# substring "whatever" in the string and so a ValueError exception will be 
# raised. 
#
# string = "To be or not to be"
# index = string.index("whatever")
# print(index)

# The rfind() method works just like the find() method except it returns the 
# index of the LAST occurrence of the substring in the string.  So below we will
# get back the index 16 because the LAST occurrence of "be" is at the index 16.
string = "To be or not to be"
index = string.rfind("be")
print(index)

# We can also use the start and end index arguments with rfind() as below we 
# will get back the index 3 back between the indexes 2 and 9 the last occurrence
# of the string "be" is at the index 3.
string = "To be or not to be"
index = string.rfind("be", 2, 9)
print(index)

# Like find() the rfind() function will return -1 if the substring cannot be
# found in the string, as is the case with "whatever" below.
string = "To be or not to be"
index = string.rfind("whatever")
print(index)

# The rindex() method behaves just like rfind(), except like the index() method 
# instead of returning -1 the method will raise the ValueError exception if the
# substring cannot be found in the string as is the case with "whatever" below.
# Uncomment the code to see what happens.
#
# string = "To be or not to be"
# index = string.rindex("whatever")
# print(index)
