################################################################################
#
# Program: Comparison Operators Examples
#
# Description: Examples of using the comparison operators in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Vw2HxT5Wj-I
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Try modifying the values of x and y below and see the effect that it has on
# the True/False boolean values that the comparison operators evaluate to
x = 5
y = 5

# Output x and y
print("x:", x)
print("y:", y)

# Equaltiy operator evaluates to true if x is equal to y, and false otherwise
print("x == y ->", x == y)

# Inequality operator evaluates to true if x does not equal y, and false
# otherwise
print("x != y ->", x != y)

# Less than operator evaluates to true if x is less than y, and false otherwise
print("x < y  ->", x < y)

# Less than or equal operator evalues to true if x is less than or equal to y,
# and false otherwise
print("x <= y ->", x <= y)

# Greater than operator evaluates to true if x is greater than y, and false
# otherwise
print("x > y  ->", x > y)

# Greater than or equal operator evaluates to true if x is greater than or
# equal to y, and false otherwise
print("x >= y ->", x >= y)

# We can chain comparison operators to make multiple comparisons.  For example
# here we check to see if z is in the range of 5 - 10 (inclusive of 5 and 10)
# using two <= operators.
z = 8
print("5 <= z <= 10 ->", 5 <= z <= 10)

# We can using comparison operators with types of values that are not numeric,
# for example to compare strings.  Strings will be considered equal if they
# exactly the same, if we were to change the w2 string to "hello" we would
# get false instead of true when using the equality operator with w1 and w2.
w1 = "Hello"
w2 = "Hello"
print("w1 == w2 ->", w1 == w2)

# Comparison operators are typically used in the conditions of control
# structures, for example in the condition of an if-statement to decide whether
# to execute a block of code or not.
a = 5
b = 2
if (a > b):
  print("a > b")