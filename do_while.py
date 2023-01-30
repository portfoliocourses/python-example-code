################################################################################
#
# Program: How To Emulate A Do While Loop
# 
# Description: Examples of how to emulate the behavior of a do-while loop in 
# Python even though the language does not officially include do-while loops. 
#
# YouTube Lesson: https://www.youtube.com/watch?v=mtX-BL1SxMw 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Many languages have do-while loop control structures like the below pseudocode
# where the loop body FIRST executes and THEN the loop condition is evaluated to
# determine whether the loop should continue to execute or not.  With a do-while
# loop, the loop body is guaranteed to execute at least once.  This is not 
# guaranteed with a while loop, where FIRST the condition is checked and THEN 
# the loop body executes if that condition evaluates to true.  Python does not
# include do-while loops, but we can emulate the functionality of a do-while 
# loop in Python. 

#      i = 10
#      do:
#          print(i)
#          i = i + 1
#      while (i < 10)

# Our desired condition for the "do while loop" is "i < 10", we set i = 10
# initially such that the condition is never true.  We create a while loop with
# condition "True" which guarantees the loop body will execute at least once. 
# The break keyword can be used to stop the execution of a loop, so we put an 
# if statement as the last statement of the loop body and when our desired 
# loop condition is NOT true we break to stop the loop!  Otherwise the loop 
# will continue until our "loop condition" is not true, just as with a regular
# do-while loop.  Except due to the while loop condition being True, the loop
# body is guaranteed to execute once.
#
i = 10
while True:
    first_iteration = False
    print(i)
    i = i + 1
    if not i < 10: break 

# Another solution would be to create a variable that will keep track of whether
# it is the first iteration of the loop, and initially set it to true.  We can 
# then make our while loop condition "first_iteration or condition" where 
# condition is our desired loop condition for a do-while loop.  Because "true or
# anything", whether 'anything' is true or false, will always be true, the loop
# body is guaranteed to execute once.  Inside the loop body we then set 
# first_iteration to false.  This means on any subsequent loop iteration the 
# while loop condition will effectively be "false or condition", and this means
# while loop condition will entirely depend on the second or operator argument.
# Because false or true is true and false or false is false, so after the first
# iteration of the loop, it will be this "desired do-while loop condition" that
# now determines whether the loop continues or not.
i = 10
first_iteration = True
while first_iteration or i < 10:
    first_iteration = False
    print(i)
    i = i + 1