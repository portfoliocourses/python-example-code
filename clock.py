################################################################################
#
# Program: Create A Clock
# 
# Description: Create a clock using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=vb7KeINPMco
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import time 

# Continue until Ctrl-C is used to stop the terminal, then output Clock Stopped.
#
# We do this to exit the program more gracefully than the KeyboardInterrupt 
# exception text that would appear on the terminal otherwise.

try:
    # Continually output the current time on the current line every second.
    #
    # strftime() will retrun the current time formatted as a string 
    # hours:minutes:seconds am/pm with hours set to 12-hour clock, this is 
    # done using the format string with the correct format specifiers:
    #
    #   https://docs.python.org/3/library/datetime.html
    #
    # We then use an f string to help output the time to the terminal.  We leave
    # a couple spaces to make space for the terminals cursor.  Instead of the 
    # default beahviour of print outputting a newline each time it outputs a
    # string, we use end="/r" to output a carriage return character instead. 
    # This will set the cursor back to the beginning of the current line of the
    # terminal, so that we overwrite whatever was there previously (the last 
    # current time, which each iteration of the loop).
    #
    # We use time.sleep(1) to pause the execution of the loop/program for one
    # second, so that we output the time each second.
    #
    while True:
        current = time.strftime("%I:%M:%S %p")
        print(f"  {current}", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.\n")        