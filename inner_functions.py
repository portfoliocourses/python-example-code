################################################################################
#
# Program: Inner Function
#
# Description: Example of using an inner function in Python, also known as a 
# nested function.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ZH8IlWHONcE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We can define an "inner function" also known as a "nested function" inside 
# another function, was the inner() function here is defined inside the 
# outer() function.

def outer(x):
  
  # creates a local variable y of the outer() function
  y = 5

  # inner functions can have their own parameters, like z
  def inner(z):
    
    # We can use z as we would a parameter of any function, e.g. to output the
    # value here...
    print("z:", z)

    # Variables like x that are in the local scope of the function 
    # outer() are what are in the "enclosing scope" of the inner() 
    # function.  We can access the values of these variables like this...
    print("x:", x)

    # If we want to modify a variable in the enclosing scope, like y which is 
    # a local variable of the function outer() but in the enclosing scope 
    # of inner(), then we need to use "nonlocal" as we do below.  This will 
    # give inner() the ability to actually modify y.  If we did not use 
    # "nonlocal y", then "y = 50" would actually create a NEW local variable
    # of the inner() function called y.
    nonlocal y
    y = 50
    print("y:", y)
    
    # We can access any variable in the enclosing scope that is created before
    # the inner function is called... here we access "a" which was created 
    # just before calling the inner function.
    print("a:", a)

    # We cannot access "b" because it is created AFTER the inner function is
    # called...
    #
    # print("b:", b)
    
    # We can create local variables of the function inner(), but they will not
    # be accessible in the outer function.
    c = 50

  
  # creates a local variable a of the outer() function
  a = 1

  # call the inner() function and pass it the value 2 as an argument
  inner(2)
  
  # Notice how the variable y of the outer() function has been modified and set
  # to 50 by the inner function...
  print("y:", y)

  # The inner() function cannot access this variable "b" because it is created 
  # AFTER the inner() function is called. 
  b = 2 

  # The outer() function cannot access a local variable of the inner() 
  # function "c", the below would cause an error...
  #
  # print("c:", c)


# Call the outer() function
outer(10)