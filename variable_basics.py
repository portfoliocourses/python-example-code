################################################################################
#
# Program: Variable Basics
# 
# Description: An introduction to the basics of using variables in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=HTCV5mD2ra0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# This will create a variable called price, and assign the value 50 to the 
# variable.  We can say that the variable price 'stores' the value 50, we can 
# think of it like a box that contains the value 50.  In Python it is more 
# accurate to describe price as a label for the value 50, technically price 
# is a *reference* to the value 50 that is stored in memory.  The value 50 
# is called an "Int" in Python as it is an integer number (a number with no
# decimal place and numbers afterwards, i.e. no fractional component).
#
price = 50

# We can create multiple variables, here we create a variable called shipping 
# and assign it the value 10.50.  The value 10.50 is not an integer, it DOES 
# have a decimal point with numbers afterwards.  This type of number is called 
# a real number in mathematics, and in Python we call it a Float, it is 
# considered a floating-point number in computing.  The '=' character is 
# really an operator called assignment, and technically the right side of 
# assignment operator is an expression that gets evaluated.
#
shipping = 10.50

# Expressions can include operators that use variables and values, here we 
# use the addition operator to add together the values of price and shipping 
# and store the result into the new variable total.
#
total = price + shipping

# We can output the value of a variable using print(variable_name).  print() 
# is actually calling a function with an argument (total).
#
print(total)

# We try to make variable names that are very descriptive to make our code 
# easier to read.  If we had called this variable 'x' it would be unclear to 
# the reader of the code what it is supposed to do, but by calling it tax_rate 
# the reader is able to better understand what the variable is storing and 
# how it may be used.  As a convention we use lowercase letters for variable 
# names and we separate words with underscore _ characters.
# 
tax_rate = 1.15

# We can change the values that variables store as a program executes, this is 
# a big reason why variables are useful as we can track and manage changes in 
# information (i.e. state) over time.  Here we use the tax rate and the 
# multiplication operator * to calculate an after tax total.
#
total = total * tax_rate 

# Output the total after the tax rate is applied.
#
print(total)

# There are many different types of values in Python, we can store text using 
# a type called strings.
#
customer_name = "Idris Elba"

# We can store True and False values using the Bool type.
#
discount = False