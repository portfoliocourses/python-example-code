################################################################################
#
# Program: Swap Two Variables
# 
# Description: An example of how to swap two the values of two variables in 
# Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=vFLr6wSePjQ 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# create two variables x and y, assign 5 to x and 10 to y, after swapping the 
# values of the variables we should have x set to 10 and y set to 5
x = 5
y = 10

# We might think the below commented code would perform a swap, but it would 
# not. The first statement would have the variable 'x' assigned the value of 'y'
# (10), and then both x AND y would be set to 10.  So when the next statement 
# executes the value of 'x' (10) would be assigned to 'y' (which is already set 
# to 10), and we're left with both x and y set to 10!  The problem is the first 
# statement will 'overwrite' the original/old value of x.
#
# x = y
# y = x 

# To perform a swap successfully we could first store the old value of x into 
# a temporary variable called old_x.  Then, instead of assigning x to y after 
# executing the x = y statement, we assign the old value of x stored in old_x 
# to y to complete the swap.  We often call the old_x variable temp to perform 
# this type of swap.  This type of swap is the standard way to perform a swap 
# in many languages.
#
# old_x = x
# x = y
# y = old_x

# In Python we can use what is called tuple assignment or multiple assignment.
# In the below statement, the expressions 'y' and 'x' on the right-hand side 
# are first evaluated to '10' and '5', and THEN those values are assigned to 
# x and y.  This completes a swap with no need for a temporary variable.
x, y = y, x

# Print out x and y to verify the swap is successful
print("x:",x)
print("y:",y)