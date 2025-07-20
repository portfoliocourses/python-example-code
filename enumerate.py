################################################################################
#
# Program: enumerate() Example
# 
# Description: Demonstrate of using enumerate in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=PO8QOxeU_No
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################ 

# Recipe steps, which are typically ordered 1,2,3,...
steps = [
    "Preheat oven to 350°F.",
    "Mix flour and sugar.",
    "Add eggs and stir well.",
    "Pour into a baking pan.",
    "Bake for 30 minutes."
]

# Looping over an iterable like a list in Python is easy enough with a for loop
#
# for step in steps:
#    print(step)

# But if we also want a counter/index variable we might use len() and range() 
# like this, which is considered less 'Pythonic' (i.e. the way to do things 
# properly in Python).  We're having to increment the counter before outputing 
# the step, call len() and range(), and use counter as a list index now.
#
# for counter in range(len(steps)):
#    print(f"Step {counter + 1}: {steps[counter]}")

# Instead we can use enumerate() which gives us back an enumerate object, which
# provides the for loop with both an auto-incrementing counter AND the next 
# item in the list/iterable with each loop body execution.  It's like an 
# iterable with a counter now.  We can also modify the starting point of the 
# counter from the default of 0 using the optional keyword parameter start.
#
for counter, step in enumerate(steps,start=1):
    print(f"Step {counter}: {step}")