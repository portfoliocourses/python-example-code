################################################################################
#
# Program: print() Function Examples
# 
# Description: Examples of using the print() function in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=VSeADGG7d6U 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################


# We can use print() to output values to user input by supplying them as an 
# argument to the function. Here we print Int, Float, String and Bool values.
# By default print will output the values to 'standard output' which will be the
# terminal/shell/command-line most typically.
print(4)
print(2.5)
print("text")
print(False)


# We can print out multiple values by supplying multiple values as arguments to
# the function, by default they will be output separated by spaces.
print("text1", "text2", "text3")


# We can output the value of variables as well by supplying them as arguments.
first_name = "Ali"
age = 20
print("Name:", first_name, "Age:", age)


# By default values are separated by spaces so this will result in: 1 2 3 4 5
print(1,2,3,4,5)


# But we can use the keyword argument 'sep' to specify different separation 
# character(s), here we use ", " which will separate the values by a comma and 
# a space so we will have as output: 1, 2, 3, 4, 5
print(1,2,3,4,5,sep=", ") 


# By default print() will output a newline character \n as the final character 
# of output, this will result in the next output appearing on the next line in
# a terminal (which is typically the behavior we would want anyways).  We can 
# use the keyword argument end to specify (a) different end character(s), here
# we set it to three spaces. So instead of:
#
# On the
# same line
#
# We get:
#
# One the   same line
#
# as output, because the first print() will output three spaces as its final 
# output instead of the newline character.
#
print("On the", end="   ")
print("same line") 


# By default print() will output to "standard output", i.e. typically the 
# terminal/shell/command-line, but we can set it to output to other places 
# such as a file.  Here we open file.txt for writing and text_file will be 
# an object we could use to write to the file.
#
text_file = open("file.txt", "w")

# We use the keyword argument file to pass in text_file as an argument to print
# and now will print will write the string "Test 1 2 3" to file.txt instead.
print("Test 1 2 3", file=text_file)

# We should close a file when we are done working with it...
text_file.close()


# Import the time module so we can use the sleep() function
import time

# Technically print() first outputs values to a buffer, and the buffer is then 
# 'flushed' when a newline character is output at which point the values are 
# output to standard output (i.e. the terminal).  Below we output ", " as the 
# end characters instead of the newline \n character.  This means that the 
# output buffer will not be flushed until the NEXT print() where we output 
# Y.  We'll be able to notice this if we use time.sleep(5) as this will pause
# execution of the program for 5 seconds.  Despite the fact that "output X" 
# is given to print() before the sleep function is called, it won't output 
# until after, because a newline character was not output, it's not until 
# the NEXT print() outputs a newline character which causes the buffer to 
# flush and the text to output.  
#
# We can provide a keyword argument flush, and if we provide True as an 
# argument this will have print() flush the buffer regardless of whether a 
# newline character is output.  You can comment out the first print and 
# uncomment the second to see what happens... instead of the "output X" 
# text outputting after sleeping for 5 seconds, it will now output BEFORE 
# because we used flush=True to have buffer flushed.  By default when we 
# use print() flush=False.
#

print("output X", end=", ")
# print("output X", end=", ", flush=True)
  
time.sleep(5)

print("then Y!")