################################################################################
#
# Program: String istitle() Method
# 
# Description: Examples of using the istitle() method in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Ig7-lA8GanA 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The istitle() method will return true if the string contains a title.  The 
# method considers a title to be a string where all words begin with an 
# uppercase letter and any letters following it are lowercase letters.

# Valid title
string1 = "The Social Network"
print( string1.istitle() )

# Invalid title, 'network' begins with lowercase letter
string2 = "The Social network"
print( string2.istitle() )

# Invalid title, 'NeTwork' contains an uppercase letter past the first character
string3 = "The Social NeTwork"
print( string3.istitle() )

# Valid title... the method will ignore characters like digits
string4 = "The Social Network 2"
print( string4.istitle() )

# Valid title... the method will ignore other characters like colon too
string5 = "The Social Network 2: Twitter"
print( string5.istitle() )