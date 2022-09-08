################################################################################
#
# Program: Comments
# 
# Description: Examples of using comments in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=JmqV3r2RH_0 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# set distance to 200         <-- we use comments like this to document our code
distance = 200

time = 40 # set time to 40    <-- we can call this an inline comment


# Python does not officially have multine comments, but we can use multiple # 
# characters (one on each line), or mutliline strings created using either 
# ''' or """ style triple quotations as done below.

#  Calculate the speed by dividing the distance    
#  by the time.

"""
  Calculate the speed by dividing the distance    
  by the time.
"""

'''
  Calculate the speed by dividing the distance    
  by the time.
'''

speed = distance / time


# We can experiment with our code by temporarily "commenting out" sections of 
# code... for example we could turn this print() below into a comment in order 
# to try out a variation (see below).  If we didn't like the new code we've 
# tried out, we still have the old code avaiable and can just uncomment the 
# code by removing the # character.
#
# print("Speed:", speed)

print("Speed ->", speed)