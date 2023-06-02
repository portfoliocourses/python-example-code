################################################################################
#
# Program: Return Multiple Values From A Function
# 
# Description: Example of returning multiple values from a function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Q2PJ-LNS3FI 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns multiple values: sum, difference and product.  We can separate the 
# values we wish to return by commas: ,.  Technically we are turning a single 
# tuple object when we do this.
def operations(x,y):
    sum = x + y
    difference = x - y
    product = x * y
    return sum, difference, product 

# Stores the 3 returned values into total, diff, and result.  Technically what 
# is happening is tuple destructuring (or "unpacking").  The 3 items of the 
# tuple are being assigned to these 3 variables.
total, diff, result = operations(50,20)
  
# Output the return values
print("total:", total)
print("diff:", diff)
print("result:", result)

# Store the return value into r as a tuple
r = operations(50,20)

# Output the tuple
print("r:", r)

# Output the type of r to confirm it is a tuple
print(type(r))
