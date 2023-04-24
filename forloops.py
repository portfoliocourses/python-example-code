################################################################################
#
# Program: For Loop Examples
# 
# Description: Examples of using for loops in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=AoiUTJrOPRw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# A for loop will repeat the execution of a block of code for each element in 
# a sequence.  A sequence is a collection of elements with an order, there are
# several built-in sequence types in Python including lists, strings, tuples
# and ranges.

# A test list of countries
countries = ["USA", "India", "Canada"]

# The for loop body (the indented print function call) will run for each element
# in the countries list, with country being set to the next string in the list 
# with each iteration (beginning with the first element, then the next element
# and so on).  This will output each country in the list.
for country in countries:
    print(country) 

# We can use for loops with any sequence type, e.g. here we output each letter
# in a string.
word = "friend"
for letter in word:
    print(letter) 

# For loops are often used with ranges, where the range type allows us to define
# a sequence of integers.  The below range will be the sequence of integers from
# 0 ... 10, so we will output the integers from 0 ... 10 below.  If we only pass
# a single integer to the range() constructor function the range will start 
# at 0 and go up to (but not including) the 'stop' integer provided as an 
# argument, incrementing ("stepping") by 1 with each number in the sequence.
for i in range(11):
    print(i) 

# Python also supports a while loop control structure that will execute a loop
# body repeatedly as long as a condition (e.g. i <= 10) is true.  We can create
# a while loop to output the integers from 0...10, as above, but to do so we 
# need to create a "counter variable" i and initialize it to 0, check the 
# counter variable with each loop iteration with a loop condition, and 
# increment the counter variable by 1 with each loop iteration.  This is more
# lines of code than the above for loop.  In general it's a good idea to use a 
# for loop when we want a block of code to execute some specific number of 
# times, and it's a good idea to use a while loop when we want a block of code
# to execute so long as some condition is true. 
i = 0
while (i <= 10):
    print(i)  
    i = i + 1

# If we supply two integers to range() then the sequence of integers will go
# from the start value (in this case 1) up until but not including the stop 
# value (in this case 11) by 1, i.e. 1,2,3,...,10.
for i in range(1,11):
    print(i) 

# We can supply an optional 3rd argument which will set a different 'step' 
# value, i.e what the numbers in the sequence will be incremented by.  So in 
# the below example i will go from 5 to 50 by 5, i.e. 5,10,15,20,...,50.
for i in range(5,51,5):
    print(i)

# Loop bodies can contain multiple statements, e.g. here below we find the
# sum of all integers from 1 ... 10 AND output teach number.
sum = 0
for number in range(1,11):
    print("number:", number)
    sum = sum + number 

# Output the sum calculate by the loop above
print("sum:", sum)

# When we put a loop inside another loop we call it a nested loop, here we 
# have m go from 1 ... 10 and then for each m value, we have n go from 
# 1 ... 10 as well and we calculate and output m x n.  So all together this 
# loop will produce 10 x 10 = 100 outputs for m from 1 to 10 and n from 1 to 10.
for m in range(1,11):
    for n in range(1,11):
        print(m, "x", n, "=", m * n) 

# continue will skip over the remainder of the loop body, so here when i is 
# equal to 5 we will not output i because the remainder of the loop body is 
# skipped (and the loop will then continue to execute as normal from there).
for i in range(1,11):
    if (i == 5):
        continue
    print(i)
 
# break will stop a loop early.  For example maybe we want to check if the 
# letter "t" is in a string, and if it is found in a string, there is no 
# sense in continuing the loop further.  So in the below example, when we 
# find "t", we break and stop the loop.  The else block of code will only 
# run IF the loop was not stopped due to a break.
for letter in "water":
    print("letter:", letter)
    if (letter == "t"):
        print("t found")
        break
else:
    print("t not found") 

# We cannot have an empty for loop body, but we can use 'pass' to create a 
# loop body that will do no work.  This might be useful when programming as a
# temporary placeholder, e.g. if we know that we need a loop but don't want 
# to write the loop body yet.
for i in range(1,11):
    pass
