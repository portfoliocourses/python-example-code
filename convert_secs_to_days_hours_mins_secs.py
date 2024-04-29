################################################################################
#
# Program: Convert Seconds to Days, Hours, Minutes and Seconds
#
# Description: Program to convert a total number of seconds into the equivalent
# number of days, hours, minutes and seconds using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=ljJejG-Q21M 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Prompt the user to enter the total seconds, convert the string the user enters
# that is returned by input() into an int value with int() and store it into 
# total_seconds.  We'll use a series of division operations done with divmod()
# to perform the conversion.
total_seconds = int(input("Seconds: "))

# If we divide the total number of seconds by 60 (the number of seconds in a 
# minute) then the quotient will be the total number of minutes and the 
# remainder will be the number of seconds left over after accounting for the 
# number of minutes.
#
# e.g. 200,000 / 60 = 3,333 remainder 20
#
# If we take that total number of minutes and divide it by 60 (the number of 
# minutes in an hour) then the quotient will be the total number of hours and
# the remainder will be the number of minutes left over after accounting for 
# the number of hours.
#
# e.g. 3,333 / 60 = 55 remainder 33
#
# And if we take that total number of hours and divide it by 24 (the number of
# hours in a day) then the quotient will be the total number of days and the 
# remainder will be the number of hours left over after accounting for the 
# number of days.
#
# e.g. 55 / 24 = 2 remainder 7
#
# So 200,0000 seconds is 2 days, 7 hours, 33 minutes, and 20 seconds

# divmod() returns the quotient and remainder, so we perform the following 
# divisions in the same pattern as the example above to obtain the equivalent
# number of days, hours, minutes and seconds
#
total_mins, secs = divmod(total_seconds, 60)
total_hours, mins = divmod(total_mins, 60)
days, hours = divmod(total_hours, 24)

# Output the resulting days, hours, minutes and seconds
print(" days:", days)
print("hours:", hours)
print(" mins:", mins)
print(" secs:", secs)