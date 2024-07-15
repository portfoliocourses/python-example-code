################################################################################
#
# Program: Multi-Line Statements
#  
# Description: Examples of how to split a statement across multiple lines using
# Python.  Explicit line joining using the line continuation character \ is 
# demonstrated, as well as implicit line joining using expressions with 
# parenthesis, square brackets and curly braces, and defining strings across 
# multiple lines with \ and docstrings (triple quote strings).  
#
# YouTube Lesson: https://www.youtube.com/watch?v=LJQ4vdI4S_4
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Python statements (or lines) are separated using newline characters (i.e. by
# hitting enter in a typical text editor)
joe_grade = 90
nageeb_grade = 95
mary_grade = 88

# We may want to split a statement across multiple lines for style reasons, 
# perhaps if a statement becomes too long to fit within the width of the 
# text editor.  We can put a line continuation \ character at the end of the 
# line and then continue the statement on the next line as below.
#
# Note that in the official Python documentation each line is referred to as a
# physical line and doing this with \ is called explicit joining of these 
# physical lines into a single logical line.
#
# Also note that we can have absolutely no characters after the \ character.
#
sum_grade = nageeb_grade + joe_grade + \
            mary_grdae

# We can also use parenthesis (), square brackets [] and curly braces {} 
# in expressions to split a statement across multiple lines.
#
# Below we split the statement across multiple lines by wrapping the 
# expression in parenthesis. 
#
sum_grade = (nageeb_grade + joe_grade + 
             mary_grade)

# A list with [] defined across multiple lines
numbers = [4, 
           5,
           6]

# A dictionary with {} defined across multiple lines   
student = {"name" : "Muhammad",
           "age" : 22}

# Strings can be defined across multiple lines using \
text1 = "A string \
across multiple lines"

# Note that the newline character before 'across...' is NOT in the above string
print(text1)

# We can use a triple quote string (or docstring) if we wish to preserve 
# newline characters
text1 = """A string 
across multiple lines"""

# Note how in this string we DO have the newline character before 'across'!
print(text1)