################################################################################
#
# Program: Assignment Operator Examples
#
# Description: Examples of using the assignment operators in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=eX6A5XVMqJk
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The assignment operator will create a variable called 'number' and the
# expression on the right-side will be evaluated (in this case to 3) and
# "stored into" number.
number = 1 + 2

# Output the value of number to confirm it is set to 3
print(number)

# Create another variable called 'other' and assign it the value of 'number'
other = number

# Output the value of other to confirm it is also set to 3
print(other)

# It might be tempting to think that the values are "stored into" the variable,
# and this terminology is used casually.  But in Python all variables are really
# labels, or more accurately, references to a value stored in memory.  So in the
# above example, both number and other reference the same value '3' in memory.
# If we only work with numeric type values this distinction may not matter, but
# if we work with things like lists or objects this distinction can become
# very important.

# list1 will refer to a list in memory with elements 1,2,3
list1 = [1,2,3]

# This will NOT create a copy of the list in memory... this will set list2 to
# refer to the SAME list in memory that list1 refers to.  So if we then
# modify list2[0] below, it will modify the SAME list in memory that list1
# refers to... we'll see this as both list1 and list2 will be output as the
# same modified list.
#
list2 = list1

# We could actually create a copy of the list in memory with list1.copy(), this
# create a duplicate list that list2 will now refer to.  THEN if we were to
# modify list2 it would not effect the list that list1 is referring to as they
# now each refer to separate lists.  It's important that we understand that
# using variables and the assignment operator does NOT create a copy, if we
# write our code with this understanding we may introduce logic bugs into our
# program when things are unexpectedly modified.
#
# list2 = list1.copy()

# If we modify list2, it will modify the same list that list1 refers to as list2
# refers to this list also!
#
list2[0] = 10

# When we output list1 and list2, we'll get the same (now modified) list with
# the first element set to '10'.  We might think that list2 = list1 would create
# a copy of "list1" and store it into list2, but this is not what the assignment
# operator does.
#
print("list1:", list1)
print("list2:", list2)


# We can assign the same value to multiple variables like this, where both q and
# w will be set to '100'.
q = w = 100

# Output q and w to confirm they are both set to 100
print("q:", q, "w:", w)


# We can assign multiple different values to multiple variables with this
# assignment operation...
q, w = 2, 8

# Output q and w to confirm that q is 2 and w is 8
print("q:", q, "w:", w)

# We can use this technique to swap the values stored in variables, here we swap
# the values of q and w.
q, w = w, q

# Output q and w to confirm the swap, that q is now 8 and w is now 2
print("q:", q, "w:", w)


# The 7 arithemtic operators:
#
#    + addition
#    - substraction
#    * multiplication
#   ** power
#    / division
#   // floor division
#    % modulus
#
# Each have an assignment operator version which combines assignment with the
# arithmetic operation.
#

# Set number to 1
number = 1

# We could add 2 to number like this... but then we would have to repeat the
# variable name 'number'
#
# number = number + 2

# Or we could use the += operator which adds 2 to the value of number and stores
# the result back into number.  This is effectively a short form version of the
# above which allows us to write more concise code.
number += 2

# Output the number to verify we have added 2 to number and now number = 3
print(number)


# Test substraction assignment operator (3 - 2 -> 1)
number -= 2
print(number)

# Test multiplication assignment operator (1 * 10 -> 10)
number *= 10
print(number)

# Test power assignment operator (10^3 -> 1000)
number **= 3
print(number)

# Test the division assignment operator (10 / 3 -> 3.33333...)
number = 10
number /= 3
print(number)

# Test the floor division assignment operator which rounds the result of a
# division operation down to the nearest integer (10 // 3 -> 3)
number = 10
number //= 3
print(number)

# Test the modulus assignment operator which returns the remainder of a division
# operation (10 % 3 -> 1)
number = 10
number %= 3
print(number)