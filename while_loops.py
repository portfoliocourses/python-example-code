################################################################################
#
# Program: While Loop Examples
#
# Description: Examples of using while loops in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=R-w-Ohf16EY
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# Basic While Loop Example
#
# A while loop will execute so long as the condition is true (in this case that
# i <= 10), repeatedly executing the loop body.  When the condition is false
# execution will jump down to the first statement after the loop (the call
# to print() to output Loop Done!).  We use the variable i as a counter variable
# to help manage the execution of the loop.  We intialize it to 1, check the
# value of i in the condition i <= 1-, and then update i with each loop
# iteration with i += 1.  This pattern of initialization, a condition, and
# an update step, is a typical pattern to see with a counter variable.  The
# loop body itself will output the value of i with each loop iteration, so we
# will output the numbers from 1-10.

i = 1

while i <= 10:
    print(i)
    i += 1

print("Loop Done!")


# Break Example
#
# We can stop the execution of a loop at any point using 'break'.  Here we
# stop the loop when i == 3.

i = 1

while i <= 10:
    print(i)
    if (i == 3):
        break
    i += 1


# Continue Example
#
# We can use the continue keyword to skip over the execution of the loop body.
# Here when i == 3 we use continue to skip over the last i += 1 statement
# in the loop body, instead after the continue statement execution will
# jump to checking the loop condition to determine if the loop body should
# execute again.

i = 1

while i <= 10:
    print(i)
    if (i == 3):
        i += 3
        continue
    i += 1


# Indeterminate Loop Example
#
# A loop does not need to use a counter variable.  For example this loop will
# execute an *unknown* number of times because we don't know when the user
# will enter 'stop'.  We call this type of loop an indeterminate loop.

# Stores string input from the user
text = ""

# Inform the user that they can enter 'stop' to quit
print("Enter 'stop' to quit")

# Continue the loop until the user enters 'stop'.  With each loop iteration the
# user is prompted to enter text, and that text is output.
while text != "stop":
    text = input("Enter Text: ")
    print(text)