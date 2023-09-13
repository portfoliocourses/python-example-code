################################################################################
#
# Program: Function Basics Examples
# 
# Description: Examples covering the basics of using functions in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Qx_Gu-9lTqc
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The function returns the feeling input by the user after greeting them.  
#
# The variable person_name is called a parameter, it will be st to the argument 
# that is supplied when the function is called.  If a person_name argument is 
# not supplied the default value for the person_name parameter will be "John". 
# The indented block of code is the "function body".  The block of code will 
# run whenever we call the function.  The return statement at the end of the 
# function is what returns the feeling value to where the function is called.
def greetings(person_name = "John"):
    print("Hi", person_name)
    print("How are you feeling?")
    feeling = input("Feeling: ")
    return feeling 
 
# We call the function with the argument "Ron", we say that we pass the argument
# to the function.  We store the returned string into the variable ron_feeling,
# and we can then use that returned value in the rest of our program.
ron_feeling = greetings("Ron")
print("Ron is feeling", ron_feeling)

# We can call a function multiple times in our code.  This allows us to repeat
# the execution of a block of code without repeating the actual block of code 
# itself in our code, which makes our code shorter, and less repetitive!
#
# harry_feeling = greetings("Harry")

# If we call greetings() without an argument, the default value for person_name
# will be used.
#
# john_feeling = greetings()


# The operations function returns the addition, difference and product of 
# two numbers.
#
# Functions can accept more than one argument and return more than one value, 
# here we have multiple parameters (x and y) and we separate them by commas.
# We separate our return values by commas as well to return multiple values.
def operations(x, y):
    return x + y, x - y, x * y 

# Here was pass the values 10 and 5 to the operations function when we call it,
# note that by passing the variable 'a' to the function what is really being 
# passed is the value 10.  We store the 3 values returned by the function 
# into the variables sum, diff and prod. 
#
# Technically what's happening here is a little more involved than what is 
# described above in a beginner-friendly way.  :-)  Technically the function
# returns a tuple and we "unpack" the tuple, see this video for more 
# details: https://www.youtube.com/watch?v=Q2PJ-LNS3FI
#
a = 10
sum, diff, prod = operations(a, 5)

# Output the returned values.
print("Sum:", sum)
print("Diff:", diff)
print("Prod:", prod)


# A function that outputs the parameter x3 value
def output(x1,x2,x3):
    print("x3:", x3)
 
# We can pass function arguments out of order by using keyword arguments, i.e. 
# by giving the parameter name = the value we wish to pass as an argument.  Here
# the x3 parameter will be set to "yes" and the others set to "no".
output(x3 = "yes", x1 = "no", x2 = "no")


# Function adds one to a value and outputs the new value.
#
# Note that the x parameter is a different variable than the x variable below 
# even though they have the same name.  The x parameter variable is 'local to 
# the function', which means it has the scope of the function, i.e. it exists 
# only in the function.
#
# In Python variables reference objects in memory.  When we pass a variable to 
# a function, what gets passed is a reference to an object, not a "copy" of 
# the value/object.  So below, when x is passed to modify, the parameter x 
# is going to reference the same Integer 10 object in memory as the variable 
# x that was passed to the function!
#
# Now Integers in Python are immutable, this means in the modify function 
# when we add 1 to x, the Integer object is not modified.  Instead a new 
# Integer 11 object is created, and the x parameter now references this new 
# object.  When we output x inside the function, we'll get '11' as output.
# 
# Notably though, the x variable outside the function is still referencing 
# the same Integer 10 object, and when we output this variable after the 
# function call, we'll get '10' as output.
#
# This is the type of behavior we can expect when we pass immutable 
# objects to a function.
#
def modify(x):
    x = x + 1
    print("x:", x)

x = 10
modify(x)
print("x:", x) 


# The function appends the value 4 to the list it is passed.
#
# Lists in Python are mutable objects.  This means we can actually 
# modify the object. 
#
# When we pass an mutable object to a function, again what's being 
# passed is a reference to the object.  So when we pass the list 'l'
# to the function, what is passed is a reference to the list, and then
# the parameter variable 'l' will reference the SAME list.
#
# So in the function when we append '4' to the list, it doesn't create 
# a new list.  Instead, '4' is added to the existing list.  This is 
# because lists in Python are mutable.
# 
# So then when we output the list 'l' after calling the function, we'll
# get [1,2,3,4], because the variable 'l' outside of the function is 
# referencing that same list that we modified IN the function.
#
# Again we need to be aware of how mutable objects will be behave
# when we pass them to a function.
#
def modify_list(l):
    l.append(4)

l = [1,2,3]
modify_list(l)
print("l:", l) 




