################################################################################
#
# Program: Logical Operators
#
# Description: Examples of using the logical operators (and, or, not) in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=0CDzyBxEVT0
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# Let's imagine that our program needs to check for TWO conditions, for example
# that a username matches a particular value AND that a password matches a
# particular value.  We'll see user and password to 'bob' and 'abc' which we'll
# imagine are the values that we're looking for.
user = "bob"
password = "abc"

# To check two conditions, we could nest an if-statement inside an if-statement,
# and if the user is 'bob' then we'll ALSO check if the password is 'abc'.
if (user == "bob"):
  if (password == "abc"):
    print("Logged In!")


# OR we could use the logical operator 'and' to check if BOTH conditions are
# true.  The below condition will only evaluate to true if the user is equal
# to 'abc' AND the password is equal to 'abc'.
if (user == "bob" and password == "abc"):
  print("Logged In!")

# The logical operator 'and' will evaluate to true when both of its operands are
# true, and false in all other cases.
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

# The logical operator 'or' will evaluate to false when both of its operands are
# false, and true in all other cases.
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

# The 'not' operator will flip False to True and True to False
print("not True:", not True)
print("not False:", not False)


# The logical operators use "lazy evaluation", which means the 2nd operand is
# only evaluated if necessary.  For example, if the first operand of the 'or'
# operator evaluates to true, then there is no need to evaluate the second
# operand because whether it is true or false the expression will evaluate to
# true.  Because 'true or true -> true' AND 'true or false -> true'.
#
# Lazy evaluation may save the computer from having to do work involved in
# evaluating the second operand, which could be a good thing!  But we should be
# aware of lazy evaluation as we can get intersting effects.  For example if we
# uncomment the below statement the program will crash with a divide by zero
# related error, because we cannot divide by zero.
#
# print( (4/0 == 0) or True )

# But the below statement will evaluate to True.  Due to lazy evaluation the
# 2nd operand, which contains the same divide by zero issue, is never
# evaluated, because the first operand is True and there is no need to evaluate
# the second operand to determine that the expression will evaluate to True.
#
print( True or (4/0 == 0) )


# The operators have the following precedence:
#
# not
# and
# or
#
# which means for example the 'not' operator will occur before the 'or'
# operator.
#
# It's important to be aware of the operator precedence, for example below
# might expect that "False or True" would evaluate first to "True" and then
# the 'not' operator would flip the "True" to "False".  But instead what happens
# is that the "not False" evaluates first to "True" and then "True or True"
# evalutes to "True".
#
print(not False or True)