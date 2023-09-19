################################################################################
#
# Program: Functions with Arbitrary Arguments
#
# Description: Examples of creating functions with an arbitrary number of 
# arguments and an arbitrary number of keywords arguments in Python.  Functions
# like these are also know as variadic functions.
#
# YouTube Lesson: https://www.youtube.com/watch?v=nb6UpZRltKU
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# - We can use *parameter_name to have a function accept an arbitrary number 
#   of non keyword arguments.
#
# - The convention is to use args for the parameter name.
#
# - The parameter will be set to a tuple containing the arbitrary number of 
#   arguments provided.
#
# - We can access and output these items with args[0], args[1], etc.
#
# - We can have parameters like x before *args.  Notice how below the 
#   argument 1 is assigned to x, and then 2 and 3 are assigned to the tuple 
#   args.
#
# - We can even have parameters like y after *args, but we need to then supply
#   the arguments as keyword arguments like y=4.
#
def arbitrary1(x, *args, y):
    print(type(args))
    print("x:", x)
    print("args[0]:", args[0])
    print("args[1]:", args[1])
    print("y:", y)

arbitrary1(1,2,3,y=4)

# - We can use **parameter_name to have a function accept an arbitrary number 
#   of keyword arguments.  This must be the last parameter in the list.
#
# - The convention is to use kwargs for the parameter name.
#
# - The parameter will be set to a Python dictionary with the keys/values of the
#   dictionary set to the keys/values of the keyword arguments.
#
# - We can have parameters like x before **kwargs and even an arbitrary number
#   of non keyword arguments with *args before **kwargs. 
#
def arbitrary2(x, *args, **kwargs):
    print(type(kwargs))
    print("x:", x)
    print("args[0]:", args[0])
    print("args[1]:", args[1])
    print("First Name:", kwargs["fname"])
    print("Age:", kwargs["age"])

arbitrary2(100, 10, 20, fname = "Joe", age = 23)