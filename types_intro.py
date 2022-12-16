################################################################################
#
# Program: Introduction To Types
#
# Description: A program to introduce the concept of types in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=37iGKq7hFCo
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create variables that will refer to values of different types
name = "Barbara Liskov"
age = 24
average = 94.59
is_student = True
grades = [92.56, 93.45, 97.78]

# The type() function returns the type of a value.  We'll find that age refers
# to an Int, name to a string (str), average to a float, is_student to a bool,
# and grades to a list.  Technically everything in Python is an object so
# we'll see "class" in the output... all objects belong to a class.
print(type(age))
print(type(name))
print(type(average))
print(type(is_student))
print(type(grades))

# There's nothing to enforce that we store integer information as int values,
# here we store the integers 41 and 50 as strings.
number1 = "41"
number2 = "50"

# Now if we try to add together number1 and number2 we'l actually get "4150"
# because with string values the + operator will actually perform string
# concatenation!
sum = number1 + number2
print(sum)

# We would need to convert the values to int values using int() to get the
# sum of the two integers (as below).  When programming it's very important
# to be aware of types in order to get the correct program behaviour.
#
# sum = int(number1) + int(number2)
# print(sum)


# Notably types exist as part of a type hierarchy, so for example Int and Float
# are both "numeric types" (we would say they are subtypes of "Numeric", along
# with "Complex" for storing complex numbers).
#
#               Numeric
#             /    |   \
#         Float   Int   Complex