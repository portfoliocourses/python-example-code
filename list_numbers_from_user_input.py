################################################################################
#
# Program: Create A List Of Numbers From User Input
# 
# Description: Approaches to create a list of numbers accepted from user input
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=KQavWedyDHE 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# There are many approaches to creating a list of numbers from user input, here
# are 3 approaches...


# Approach #1 - Prompt the user for the total amount of numbers, then use a loop
# to input this many numbers.

# Begin with an empty list
numbers = []

# Prompt the user for the total amount of numbers to be entered (we use int() to 
# convert the string returned by input() to an int value).
total = int(input("Total Numbers: "))

# Output an error if the total is negative, we can't have a list with a negative
# amount of numbers
if total < 0:
    print("Cannot enter negative total numbers")
else:
    # Otherwise this will run 'total' amount of times with i going from 1 to 
    # total by 1 with each loop iteration.  We prompt the user to enter each 
    # number with "Number 1: ", "Number 2: " and so on (converting i to a string
    # with str() and concatenating the strings with +).  We append the converted
    # int value (done again with int()) to the numbers list.
    for i in range(1, total+1):
        number = int(input("Number " + str(i) + ": "))
        numbers.append(number)

# Output the numbers list
print(numbers)


# Approach #2 - Prompt the user to enter numbers and append them to a list until
# they enter a special "sentinel" value that indicates they wish to stop 
# inputting numbers.

# Begin with an empty list
numbers = []

# Each time the loop condition is evaluated the user will be prompted to enter
# a number using input(), and number will be assigned the string they enter
# using the walrus operator (:=). The walrus operator will ALSO result in 
# the expression as a whole (number := input ....) evaluating to whatever was
# assigned to number, which we then check if it does not equal the string "q".
# So as long as the user enters in integers like 4,5,etc they will not equal
# "q".  But once the user enters in the special sentinel value "q" the 
# loop will stop because "q" == "q" and the condition is false.  Each time 
# the user enters a number we append it to the numbers list.
# 
while (number := input("Number (q to quit): ")) != "q":
  numbers.append(int(number))

# Output the resulting numbers list
print(numbers)


# Approach #3 - Ask the user to enter all the numbers at once separated by 
# spaces and use a list comprehension to create a list of the entered numbers. 

# Calling input() prompts the user to enter in a list of numbers separated by 
# spaces, which will result in a string like this if the user enters in 9, 8
# and 7: "9 8 7".  The split() method will then split the string into a list
# of string separating them according to the spaces in the original string, 
# so for the above string we would then have ["9", "8", "7"].  Finally the 
# list comprehension [int(s) for .... ] will then take each of these strings
# and return the list that results in applying the int() function to each one
# of them (converting them all to int values).
#
l = [int(s) for s in input("List (1 2 ...): ").split()]

# Output the resulting list
print(l)