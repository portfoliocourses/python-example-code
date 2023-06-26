################################################################################
#
# Program: Output To Standard Error Example
# 
# Description: Examples of ways to output to the standard error stream using 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=b09D3pG6jQc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import sys
import logging

# By default when using print() the string will be output to standard output
print("Standard output")

# If we import the sys module and supply file=sys.stderr as a 2nd argument then
# the string will be output to the standard error stream
print("Standard error", file=sys.stderr)

# We can also use the write() method of stderr in the sys module, but the 
# be aware the write method does not put a newline at the end of the string 
# we output as the print() function does by default.
sys.stderr.write("Error message\n")

# We can also use the logging module to output to standard error, here the 
# warning function will write the "Warning message" to standard error.
logging.warning("Warning message")
