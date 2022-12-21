################################################################################
#
# Program: Type Conversion Examples
#
# Description: Examples of type conversion in Python (i.e. type casting),
# including examples of int(), float() and str() built-in type conversion
# functions.
#
# YouTube Lesson: https://www.youtube.com/watch?v=20WigvWJ8JA
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# IMPLICIT TYPE CONVERSION EXAMPLE

# Sometimes values will be implicitly converted from one type to another type
# as a Python program executes.

# Create two variables x and y and initialize them to 2 and 3.5
x = 2
y = 3.5

# x is of type int
print("x:", x)
print("type(x):", type(x))

# y is of type float
print("y:", y)
print("type(y):", type(y))

# When we add together x and y with the + operator x will be implicitly
# converted to a float value in order for float addition to occur
z = x + y

# Notice that z is of type float
print("z:", z)
print("type(z):", type(z))


# EXPLICIT TYPE CONVERSION EXAMPLES

# We can use built-in Python functions int(), float() and str() to perform
# explicit type conversions between types.


# We can use float() to convert an int to a float

# ai will be of type int
ai = 2
print("ai:", ai)
print("type(ai):", type(ai))

# af will be of type float
af = float(ai)
print("af:", af)
print("type(af):", type(af))

# We can also use float() to convert a string to a float

# b will be of type float
b = "2.45"
print("b:", b)
print("type(b):", type(b))

# We can re-assign the return value of float() back to the same variable, and
# in this case b will now be a float value instead of a string after conversion
b = float(b)
print("b:", b)
print("type(b):", type(b))


# We can use int() to convert a string to an int

# Note that the string does need to contain a valid integer, if we tried to
# convert this string to an int we would get an error
# xs = "5.25"

# xs will be of type string
xs = "5"
print("xs:", xs)
print("type(xs):", type(xs))

# xi1 will be of type int
xi1 = int(xs)
print("xi1:", xi1)
print("type(xi1):", type(xi1))

# We can also use int() to convert a float to an int

# xf will be of type float
xf = 5.25
print("xf:", xf)
print("type(xf):", type(xf))

# xi2 will be of type int and we'll get the value 5, the fractional portion of
# the number .25 is "lost" in the conversion, sometimes when we perform type
# conversions information loss may occur.
xi2 = int(xf)
print("xi2:", xi2)
print("type(xi2):", type(xi2))


# We can use str() to convert an int to a string

# yi will be of type int
yi = 7
print("yi:", yi)
print("type(yi):", type(yi))

# ys1 will be of type string
ys1 = str(yi)
print("ys1:", ys1)
print("type(ys1):", type(ys1))

# We can also sue str() to convert a float to a string

# yf will be of type float
yf = 7.25
print("yf:", yf)
print("type(yf):", type(yf))

# ys2 will be of type string
ys2 = str(yf)
print("ys2:", ys2)
print("type(ys2):", type(ys2))

# We can also use str() to convert values of other types to a string, for
# example we can convert a list to a string

# the list [1,2,3] will be converted to a string
slist = str([1,2,3])
print("slist:", slist)
print("type(slist):", type(slist))

# Notably there are other built-in Python functions for performing type
# conversions, but those will be covered in other tutorials related to those
# data types.