################################################################################
#
# Program: Accepting User Input With input()
#
# Description: Examples of accepting user input with input() in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=DlR14-bm3Ck
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# input() will output the text "Name: " to the terminal and then pause the
# program for the user to enter in a sequence of characters until the users
# hits the "Enter" key.  At that point the string of characters that the user
# has entered will be returned by the input() function as a string value, and
# name will store this string (technically speaking, name will 'reference' the
# string, but let's not worry about that distinction right now).
name = input("Name: ")

# When we store the value entered by the user into a variable, we can use the
# data again later in our program.  Here we do so by outputting the name that
# was entered to say hello to the user.
print("Hello", name)

# We can accept multiple user input values, here we prompt the user to enter in
# their age, and we store the entered value into the age variable.
age = input("Age: ")

# We can ouput how old the user is
print("You are", age, "years old")

# The input() function returns a string value.  If we want to treat that value
# as an integer so we can add 1 to it, in order to tell the user how old they
# will be next year, we would first need to convert that string value to an
# int.  Here we pass the age string value to the int() function, which returns
# the int value of that string, so if the string is "55" the int value will
# be 55.
age_number = int(age)

# We can then use this new int value to perform an addition operation, adding 1
next_year = age_number + 1

# We can then output how old the user will be next year
print("Next year you'll be", next_year)

# There are other types of input we may want to accept, such as floating-point
# numbers (i.e. floats) which are numbers that contain decimal place values.
# Here we call float() passing it the string value returned by input() to
# convert the string to a float, and then store it into price.
price = float(input("Price: "))

# Calculate the after tax price, assuming the tax is 10%
after_taxes = price * 1.10

# Output the after tax price
print("After Tax:", after_taxes)