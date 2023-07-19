################################################################################
#
# Program: Convert A Temperature From Celsius To Fahrenheit
#
# Description: Program to convert a temperature from Celsius to Fahrenheit 
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=LQ6hIkKjLrQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter the temperature in Celsius using input(), the 
# function will return the text entered by the user as a string, convert that 
# string to a float value with float() and store it into celsius (so that we 
# can perform mathematical operations with the value).
celsius = float(input("Temperature (C): "))

# Convert the temperature from celsius to fahrenheit using the formula:
# https://en.wikipedia.org/wiki/Fahrenheit
fahrenheit = celsius * 1.8 + 32

# Output the temperature in Fahrenheit
print("Temperature(F):", fahrenheit)

# Alternatively, we could use an f-string to output the temperature with 
# 2 decimal digits of precision.
print(f"Temperature (F): {fahrenheit:.2f}")