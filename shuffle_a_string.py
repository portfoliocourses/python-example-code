################################################################################
#
# Program: Shuffle A String
#
# Description: A program to shuffle a string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=FmL0iAJRHDs 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Imported so we can use the sample() function
import random

# A test string
s = "PortfolioCourses.com"

# random.sample(X,N) will randomly select N characters from the string X and
# return them in a list.  We pass our string s as the first argument and the 
# LENGTH of the string as the second argument (i.e. number of characters in 
# the string), so that the function returns a list of all the characters in 
# the string in a random order.  We then use the string join method to join 
# these list items together into a new string, separated by the empty string ""
# (i.e no separation between the list items), giving us a shuffled string.
#
shuffled = "".join(random.sample(s, len(s)) )

# Output the shuffled string
print(shuffled)