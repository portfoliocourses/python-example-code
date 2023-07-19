################################################################################
#
# Program: Convert A Temperature From Fahrenheit To Celsius 
#
# Description: Program to convert a temperature from Fahrenheit to Celsius  
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=i7UP4FU8twY 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter the temperature in Fahrenheit using input(), the 
# function will return the text entered by the user as a string, convert that 
# string to a float value with float() and store it into fahrenheit (so that we 
# can perform mathematical operations with the value).
fahrenheit = float(input("Temperature (F): "))

# Convert the temperature from fahrenheit to celsius using the formula:
# https://en.wikipedia.org/wiki/Celsius
celsius = (fahrenheit - 32) / 1.8

# Output the temperature in Celsius
print("Temperature (C):", celsius)

# Alternatively, we could use an f-string to output the temperature with 
# 2 decimal digits of precision.
print(f"Temperature (C): {celsius:.2f}")