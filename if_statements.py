################################################################################
#
# Program: If Statement Demonstration
#
# Description: Examples of using if-statements in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Ps67yK52Kxk
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# Try altering what the variable age is set to below and see the effect that it
# has on the program output to help understand the code below!
age = 55


# Basic if-statement example
#
# If the conditional expression 'age < 18' evaluates to true the block of code
# for the if-statement will execute, otherwise it will not.  The block of code
# is created by indenting the statements, in the Python community it is
# recommended to indent by 4 spaces.
#
if age < 18:
    print("User is a child")
    print("User cannot vote")

# If we only have a single statement, we don't need a block, we can put the
# statement after the : like this and it will execute if the condition is true.
#
if age < 18: print("User is a child")


# If-statement with else case example
#
# If the condition age < 18 is true, the block of code below this condition
# will execute, but if the condition is false the block of code below the
# "else case" will execute.  Only one block or the other will execute, never
# both.  But we can use else case to execute code if the condition of an
# if-statement is NOT true.
#
if age < 18:
    print("User is a child")
    print("User cannot vote")
else:
    print("User is an adult")
    print("User can vote")


# If-statement with elif cases and else case
#
# We can also have 'elif' (else if) cases.  If the first condition age < 18 is
# true, then the block of code below it will execute.  But if it is false, then
# the next elif case condition will be evaluated (age >= 100), and if this
# condition is true the block of code below it will execute.  Otherwise the
# NEXT elif condition will be evaluated (age >= 65), and if this condition
# is true then block of code below it will execute.  Otherwise if it is false,
# the block of code for the else case will execute.
#
# We can have as many elif cases as we like.  The if & elif case conditions will
# be checked from top to bottom, and the first case that is true will have
# its block of code executed.  If NO conditions are true, then the block of code
# for the else case will execute.  Only one block of code will execute, even
# if multiple conditions are "true".  Because conditions are checked from top
# to bottom, the FIRST condition that is true will have its block of code
# executed even if other conditions are technically "also true".
#
if age < 18:
    print("User is a child")
    print("User cannot vote")
elif age >= 100:
    print("User is over 100!")
elif age >= 65:
    print("User is a senior")
    print("User can vote")
else:
    print("User is an adult")
    print("User can vote")

# After an if-statement is done its work, execution will jump to the first
# statement after the if-statement.  So no matter which block of code of the
# above if-statement is executed, afterwards this statement will execute.
print("If Done!")


# It is common to see the logical operators 'and', 'or' and 'not' used to create
# compound conditionals.  For example here we check to see if the age is
# greater than or equal to 18 AND if the age is less than or equal to 65 using
# the 'and' operator, and the condition will evaluate to true only if BOTH of
# these expressions evaluate to true.
#
if age >= 18 and age <= 65:
    print("User age is valid")


# A short-form version of the if-statement exists.  Here we use it to ouput
# either "A" or "C".  It is equivalent to the below "long-form" version (other
# than the capitalization of the letters).
#
print("A") if age >= 18 else print("C")

# "Long-form" if-statment equivalent to the above statement
if (age >= 18): print("a")
else: print("c")


# Sometimes the short-form version of the if-statement is referred to as the
# "ternary operator" as it will evaluate one expression OR the other as the
# ternary operator does in some langauges (e.g. C, C++).  So the below
# "True if age >= 18 else False" will evaluate to either "True" or "False" and
# the result will be stored into the variable 'adult'.
#
adult = True if age >= 18 else False

# Output adult to verify the result of the above statement
print(adult)