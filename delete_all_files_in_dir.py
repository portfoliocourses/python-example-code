################################################################################
#
# Program: Delete All The Files In A Directory
# 
# Description: A program to delete all the files in a directory using Python 
# with functions in the built-in os module.
#
# YouTube Lesson: https://www.youtube.com/watch?v=61Mhj94-0I8 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# import the os module which includes helpful functions for working with files 
# and directories
import os

# The path of the directory where we want to delete all the files, ./ is the 
# current working directory
path = "./"

# The listdir() function will return a list of all the files and directories in
# directory stored in path, we'll loop through each of these setting name to 
# each file/directory
for name in os.listdir(path):

    # Build the path to the file or directory by concatenating the name to the
    # directory path
    file = path + name 

    # The path.isfile() function will return true if the path we've constructed
    # above is a path for a file, otherwise it will return false.  If we have a
    # file, we delete it using the remove() function.
    if os.path.isfile(file):
        os.remove(file)