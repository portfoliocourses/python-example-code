################################################################################
#
# Program: Countdown Timer
# 
# Description: A countdown timer to countdown a specified number of seconds 
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=rjsUETNABqc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The sleep() function from the time module can pause the program for one 
# second at a time
from time import sleep

# Prompt the user to enter the number of seconds for the timer, convert the 
# string entered into an int and store it into seconds
seconds = int(input("Enter Seconds: "))

# If the seconds entered is greater than 0 we can create a countdown timer
if seconds > 0:
    
    # The loop will continue so long as the timer has not gone below zero
    while seconds >= 0:

    	# To nicely format the time, obtain the number of minutes and econds
    	# remaining by using divmod() with seconds and 60 as arguments.  This
    	# will return the quotient (number of minutes) and remainder (number 
    	# of seconds after accounting for minutes) by dividing seconds by 60.
        mins, secs = divmod(seconds, 60)

        # Format a nice string with time in mm:ss format, with two leading 
        # zeros for each number so we'll get say 00:05 if there are 5 secs
        # remaining
        time = "   {:02d}:{:02d}".format(mins,secs)
        
        # Output the time string... instead of outputing \n after the string as
        # is the default with print(), which would cause each time to output on
        # a new line, instead we'll about a carriage return character \r which
        # will cause the next time to be output on the SAME line.
        print(time, end="\r")

        # Pause the program for one second so that each loop iteration takes 
        # 1 second as the timer should
        sleep(1)

        # Subtract one from seconds as another second has now elapsed
        seconds -= 1

# if seconds is <= 0 output an error message as a timer with <= 0 seconds does
# not make sense
else:
    print("Seconds must be greater than 0") 