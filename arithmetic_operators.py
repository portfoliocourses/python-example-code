################################################################################
#
# Program: Arithmetic Operators
#
# Description: Examples of using the arithmetic operators in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=rDlKZPZP0sM 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create variables 'a' and 'b' and set them to 2 and 5 so we can test out the
# arithmetic operations
a = 5
b = 2

# Output the values of 'a' and 'b'
print("a =", a)
print("b =", b)
print("")

# Addition operator
print("   a + b =", a + b)

# Subtraction operator
print("   a - b =", a - b)

# Multiplication operator
print("   a * b =", a * b)

# Power operator ('exponentiation')
print("  a ** b =", a ** b)

# Division operator
print("   a / b =", a / b)

# Modulus operator... returns the remainder of a division operation
print("   a % b =", a % b)

# Floor division... rounds division result down to the nearest integer
print("  a // b =", a // b)

# Here the result of floor division will be negative as we are dividing by
# *negative* b, and we might expect -2 as 5/2 above will give us 2.  But
# floor division rounds down to the next LOWEST integer, and the next lowest
# integer from -2.5 is -3, -2 would be the next highest integer.  This
# behavior can sometimes confuse people as they expect // to round towards zero.
# Also note that in the below example that -b is using the negation operator to
# get the negation of b, the negation operator is a 'unary operator' because it
# is applied only to one operand.
#
print(" a // -b =", a // -b)

# Create variables 'c' and 'd' and set them to 4 and 5 so we can test out the
# shortform assignment operator.
c = 4
d = 5

# Output the values of 'c' and 'd'
print("")
print("c before =", c)
print("d before =", d)

# Each arithmetic operator has an associated short-form assignment operator that
# will apply the arithmetic operator and then assign the result to the leftside
# variable/operator.  So for example the below is equivalent to:
#
# c = c * d
#
c *= d

# Output c after applying the above operation.  Note that equivalent operators
# +=, -=, etc, exist for all the other arithmetic operations.
print(" c after =", c)

# Operators will be applied with a defined precedence.  So by default the
# multiplication operator will be applied before addition and with...
#
# result = 5 * 2 + 8
#
# ...we would expect to get back 18 as 5 * 2 will first give us 10, and then
# 10 + 8 will give us 18.  We can use brackets to enforce a particular
# order, as we do below to ensure the addition operation is applied first.  But
# we need to be aware that operators have a defined precedence in Python.
#
result = 5 * (2 + 8)

# Output the result
print("result =", result)
