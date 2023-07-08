################################################################################
#
# Program: sleep() Function Examples
# 
# Description: Examples of using the sleep() function in Python to pause the 
# execution of the program (i.e. the current thread).
#
# YouTube Lesson: https://www.youtube.com/watch?v=P6-dtMFWPLw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# We need to import the time library
import time

# Or we can import the sleep function from time like this..
# 
# from time import sleep
#
# If we do this it is unnecessary to have time. before calling sleep() as we 
# do below, we can just have sleep(2), etc.

print("program start")

# This will pause the execution of the program for 2 seconds
#
# sleep(2)

# This will pause the execution of the program for 0.5 seconds, as the function
# allows us to supply float values as an argument to pause the program for 
# fractions of a second.
#
# sleep(0.5)

# This will pause the execution of the program for 1 second after outputting
# each integer 
for i in [1,2,3,4,5,6,7,8,9,10]:
  print(i)
  time.sleep(1)

print("program end")