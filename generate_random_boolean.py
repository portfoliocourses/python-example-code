################################################################################
#
# Program: Generate A Random Boolean
#
# Description: Techniques to generate a random boolean using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=p4SpxIOj0jE
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# All techniques will use functions in the random module
import random

# Technically we could improve performance with the below import of getrandbits
# (and/or choice if we use the 1st technique) instead of "import random" because
# one less name lookup would be required.
#
# from random import getrandbits

# choice() will return True or False randomly, this technique is very readable  
value = random.choice([True,False])

# While less readable we can improve performance using getrandbits(1) which will
# return a non-negative integer with 1 bit randomly set (so the integer will be
# either 0 or 1).  When we use bool() to convert the returned 1 or 0 to a bool 
# we will get True (for 1) or False (for 0).
value = bool(random.getrandbits(1))

# We can improve performance more by using the not operator, as not 1 will 
# result in False and not 0 will result in True.
value = not random.getrandbits(1)

# If we used the 2nd form of import above commented out, this would also improve
# performance, and we would then call the function like this...
#
# value = getrandbits(1)

# Output the generated boolean (note that we should comment/uncomment the above
# statements to test out the different methods).
print(value)