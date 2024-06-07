################################################################################
#
# Program: Count The Words In A File
# 
# Description: Program to count the words in a file using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=Xofj7X5ZoPc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import string

# Return the count of the words in the file with the provided filename
def count_file_words(filename):
    
    # open the file for reading, file is an object which allows us to access
    # the file
    with open(filename) as file:
        
        # Read all file text and store into text as a string using read() method
        text = file.read()

        # Filters out all punctuation marks in the original string.  The 
        # translate() method will take text and return a new string created 
        # using the translation table created by str.maketrans().  The 
        # str.maketrans() method could be used to replace characters with other 
        # characters in the string but we pass in empty strings as the first 
        # two arguments as we aren't going to do this.  We do pass in 
        # string.punctuation as the third argument, a string constant contained 
        # in the string module containing all punctuation mark characters.  
        # This optional third argument will have all the characters of this 
        # string (string.punctuation) removed from text.
        #
        # We remove these punctuation marks because we don't want something like
        # a dash character '-' to be considered a word.
        #
        after = text.translate(str.maketrans('','',string.punctuation))

        # We split the string wherever there are whitespace characters like ' ', 
        # '\n' and '\t' using after.split() which will give us a list of string 
        # items like: ['9', 'words', 'separated', ... and on ... ].  We don't 
        # want numbers like '9' to be considered a word.  So we take this list 
        # and use it in a list comprehension, where we produce a new list 
        # containing only the original list items that are ONLY made up of 
        # alphabetic characters. The isalpha() string method will only return 
        # true if the string is only made up of alphabetic characters, and so 
        # we use this to do the filtering.
        #
        words = [word for word in after.split() if word.isalpha()]
    
        # Find the number of items in the list using len(), i.e. number of words
        # in the string
        total_words = len(words)
        
        # Return the word count
        return total_words


# Prompt the user to enter a filename, store input value into entered_filename
entered_filename = input("File: ")

# Output the returned word count for the entered filename
print(count_file_words(entered_filename))