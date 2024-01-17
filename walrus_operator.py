################################################################################
#
# Program: Walrus Operator Examples
#
# Description: Basic examples of using the walrus operator in Python, also 
# officially known as the assignment expression operator.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Y5rDTHve8M4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The walrus operator := will assign a value to the variable (in this case 1)
# but also return the value assigned to the variable (1) to the expression in
# which it is used, so this will become y = 1 + 1 and y will be set to 2 and
# x to 1 by the below statement.
y = 1 + (x := 1)
    
# x will be 1 and y will be 2
print("y:", y)
print("x:", x)

# Notably we can't have this...
#
# y = 1 + x := 1
#
# Python syntax will not allow for it.  The walrus operator has lower precedence
# than everything but the comma, so the above expression would be like trying 
# to add "x := 1" to 1, which doesn't make sense.

# By design the walrus operator can't be used in the exact same places and ways
# as the assignment statement, so if we want to assign a value to a variable 
# like the below we can't do it exactly like an assignment statement with 
# z := 5, we would need brackets to make it work...
#
(z := 5)

# The above will work and z will be set to 5
print("z:", z)


# If we want to prompt the user to enter numbers and append those numbers 
# to a list until the user enters -1, without using the walrus operator 
# we might do it like this...

# Create an empty list
data = []

# Continue the loop until we use break to stop the loop
while True:

    # Prompt the user to enter the number and store it into number
    number = int(input("Enter number (-1 to quit): "))

    # Stop the loop with break if the number -1 was entered
    if number == -1:
        break

    # Append the number to the list
    data.append(number)

# Output the list
print(data)


# Using the Walrus operator we can shorten the above code by prompting the 
# user to enter the number right inside the while loop condition and 
# assigning the result, using the walrus operator, to number.  Then because
# the walrus operator will return the value assigned to number, still as 
# part of the while loop condition, we can check to see if the user did 
# not enter -1, in which case we want to continue the loop.  The loop body
# now simply appends the number to the list.  This saves us 3 lines of 
# code and arguably makes the code simpler/easier to follow (though of 
# course this is subjective).

data = []

while number := int(input("Enter number (-1 to quit): ")) != -1:
    data.append(number)
   
print(data)