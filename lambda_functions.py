################################################################################
#
# Program: Lambda Functions
#
# Description: Examples of lambda functions in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=N4aphT88u78
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Lambda functions are a special type of small anonymous function in Python.
#
# We define a lambda function using:
#
#    lambda [parameters] : expression
#
# Where [parameters] could be empty, or it could be a single parameter like 
# "x" or multiple parameters like "x,y,z".  The return value of the function 
# is the result of the expression.  Lambda functions cannot contain statements
# like if-statements, or be used with annotations.
#
# The below defines a lambda function that adds one to the parameter x.  We 
# assign the lambda function to the variable add_one so we can use add_one 
# as a name for the function.
#
add_one = lambda x : x + 1

# This function is equivalent to this function below...
#
# def add_one(x):
#     return x + 1

# Call add_one and pass it 5 as an argument, we'll get 6 back as a result, which
# we output using print.
print(add_one(5))

# We could have a lambda function with NO parameters like this that simply 
# returns 10...
#
# add_one = lambda : 10

# Lambda functions don't have a name, that's why we call them anonymous 
# functions.  Below we define a lambda function with two parameters x,y which 
# we separate using commas, and the lambda function returns the product of x and
# y.  We then *call* this function we've defined by surrounding it with brackets
# ( ... ) and passing the arguments 10 and 5 and with (10,5).
#
print( (lambda x,y : x * y)(10, 5) )

# Define a list of numbers
numbers = [1,2,3,4]

# Define a function that double's the number its passed
def double(x):
    return x * 2

# We could double the numbers in the numbers list by passing the double 
# function to map along with numbers.  The map function will call the double 
# function for each number in the numbers list, with each number being passed to
# the function one after the other, and map() will return a map object 
# containing the returned values.
#
# doubled = map(double, numbers)

# One use case for lambda functions is to avoid having to create a function with
# a name for simple cases like this where we need a simple function that we will
# use only one place in our code.  We could just define and pass a lambda 
# function to map "inline" like this, saving space and making our code 
# potentially easier to read as all the information is on one line.
#
doubled = map(lambda x : x * 2, numbers)
 
# Convert the doubled map to a list and output the doubled numbers
print(list(doubled))