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

string = "To be or not to be"
index = string.find("be")
print(index)

string = "To be or not to be"
index = string.find("o")
print(index)

string = "To be or not to be"
index = string.find("X")
print(index)

string = "To be or not to be"
index = string.find("whatever")
print(index)

string = "To be or not to be"
index = string.find("o", 4)
print(index)

string = "To be or not to be"
index = string.find("be", 2, 5)
print(index)

string = "To be or not to be"
index = string.find("be", 2, 4)
print(index)

string = "To be or not to be"
index = string.index("not")
print(index)

string = "To be or not to be"
index = string.index("o", 3, 9)
print(index)

# string = "To be or not to be"
# index = string.index("whatever")
# print(index)

string = "To be or not to be"
index = string.rfind("be")
print(index)

string = "To be or not to be"
index = string.rfind("be", 2, 9)
print(index)

string = "To be or not to be"
index = string.rfind("whatever")
print(index)

# string = "To be or not to be"
# index = string.rindex("whatever")
# print(index)
