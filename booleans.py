################################################################################
#
# Program: Booleans
# 
# Description: Example of using boolean data type values in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=TB9pLwACG5Y 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Boolean values are either True or False
x = True 
y = False

# We can use type() to verify x and y are boolean values
print(type(x))
print(type(y))

# Many operators such as the comparison operators like less than '<' will 
# produce a boolean values as a result 
result = 3 < 5
print("result:", result)

# Logical operators like 'or' produce a boolean as a result
result = True or False 
print("result:", result)

# The membership operators like 'in' produce a boolean as a result
result = 5 in [1,2,3]
print("result:", result)

# The identity operators like 'is' produce a boolean as a result
result = 1 is 1
print("result:", result)

# Booleans are used in the conditions of control structures if, while
a = 2
b = 3

# The condition expression is evaluated and if it is true the block
# of code executes (otherwise the else block executes)
if (a <= b):
  print("a <= b")
else:
  print("a > b") 

# The condition expression is evaluated and so long as it is True the 
# loop body will continue to execute
while a <= b:
  print(a)
  a = a + 1 

# We can have functions return a boolean value
def lucky_number(number):
  return number == 7

# This will result in the value True being returned
print(lucky_number(7))

# We can use bool() to convert a value to a boolean
converted = bool("abc")
print("converted:", converted)

# By default, most values are True.
# 
# False values include:
#
#   - the number 0 (or 0.0, 0j)
#   - empty strings, lists, tuples, sets,
#     dictionaries, ranges
#   - None

# Non-boolean values will evaluate to a boolean when used in contexts
# like an if-statement condition or while loop condition
if (""):
  print("String is not empty")
else:
  print("String is empty")

# By default, an object is considered true unless its class defines 
# either a __bool__() method that returns False or a __len__() method 
# that returns zero, when called with the object.

# So we can define a Car class with a __bool__() method that returns True
# if the fuel is > 0
class Car:

  def __init__(self):
    self.fuel = 0

  def __bool__(self):
    return self.fuel > 0

# We can instantiate a Car object 
car = Car()

# And now if we use car where a boolean is expected in the if statement 
# condition, it will evaluate to True or False depending on the __bool__()
# function we have defined.
if (car):
  print("Fuel is not empty") 
else:
  print("Fuel is empty")