################################################################################
#
# Program: global Keyword Examples
# 
# Description: Examples of using the global keyword in Python which allows us 
# to create and assign to global variables inside of functions.
#
# YouTube Lesson: https://www.youtube.com/watch?v=-t52p5pMAGU
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Using the keyword global outside a function has no effect, we can create a 
# global variable x simply by assigning to it.
global x
x = 20

def function():

  # This will allow the function to assign to the global variable x
  global x

  # If we did not have the statement above, this statement would actually 
  # create a NEW variable x that is local to this function
  x = 10

  # Output the value of the variable x
  print("x function:", x)
  
  # global can also be used to create global variables inside of a 
  # a function, here we create a new global variable called new_variable
  global new_variable
  new_variable = 200

  # The global keyword can also be used to create and assign to global 
  # variables inside of inner() functions, uncomment the below code to 
  # see the effect.
  #
  #  def inner():
  #    global x
  #    x = 30
  #    print("x inner:", x)
  #
  #  inner()


# If we try to access new_variable before calling the function it won't yet
# exist because the function is what creates it!  Uncomment the below 
# statement to see...
#
# print("new_variable:", new_variable)

# the function will modify the global variable x and set it equal to 10
function()

# We can output x to see it is now set to 10.  Try to comment out the 
# "global x" statement inside the function to see the difference.
print("x outside:", x)

# The call to the function will create the global new_variable
print("new_variable:", new_variable)