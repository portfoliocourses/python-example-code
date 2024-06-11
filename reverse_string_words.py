################################################################################
#
# Program: Reverse The Words In A String
# 
# Description: Program to reverse the words in a string using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=wcZRSbtBzGc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns a new string identical to text but with the words contained in the 
# string text reversed
def reverse_words(text):

    # Keeps track of whether a word is currently being read
    reading_word = False

    # The new string returned by the function which we'll build as we go 
    # though the text string
    reversed_words_text = ""

    # A reversed version of the current word being read
    current_word = ""

    # The string is read one character at a time, and as it is we keep track of
    # whether a word is currently being read or not.  We do this because if a 
    # word is currently being read, we'll build a reversed version of that word
    # in current_word.  When we reach the end of the word, we'll concatenate 
    # that reversed version of the word onto the new string reversed_words_text.
    #
    # We consider words to be made up of a sequence of 1 or more alphabetic 
    # characters (as detected using isalpha()) and non-alphabetic characters 
    # to be non-word characters.
    # 
    for character in text:

        # If we are NOT currently reading a word AND we have an alphabetic 
        # character, this is the beginning of a new word.  We set reading_word
        # to True to recognize this and store this first character into 
        # current_word.
        if character.isalpha() and not reading_word:
            reading_word = True
            current_word = character 

        # If we ARE currently reading a word AND we have an alphabetic character
        # then it must be the next character in this word.  We concatenate it on
        # to the front of the current_word string (which has the affect of 
        # reversing the word one character at a time).
        elif character.isalpha() and reading_word:
            current_word = character + current_word 
        
        # If we ARE currently reading a word AND we have a non-alphabetic 
        # character then we have reached the end of the word.  We set 
        # reading_word to False to recognize this, we concatenate the completed
        # reversed word to the reversed_words_text string, and we also 
        # concatenate this next non-word character after the word.
        elif not character.isalpha() and reading_word:      
            reading_word = False
            reversed_words_text += current_word
            current_word = ""
            reversed_words_text += character 

        # Otherwise we must not be currently reading a word and the character
        # must not be alphabetic, as would be so in the ' ' character after 
        # the ',' in the string below.  In this case we just concatenate the 
        # character to the reversed_words_text string.
        else:
            reversed_words_text += character 

    # If the string ends with a word and not a non-alphabetic character (like 
    # the below string ends with 'words'), then the end of the word will not
    # be detected with the else if block above which relies on detecting the 
    # first non-alphabetic character after the word (and in this case, there 
    # is none).  So in the case that the string ends with a word, current_word
    # will be non-empty after the for-loop runs, it will store the reversed 
    # version of that word, and we just concatenate that word to the 
    # reversed_words_text string.  
    #
    # Note that in Python if the string current_word is NOT empty then the 
    # below condition evaluates to True (but if it IS empty it evaluates to 
    # False).
    if current_word:
        reversed_words_text += current_word 

    # Return the string built above
    return reversed_words_text


# Test the function with an example string and output the results
example = "A string, with several words"
reversed = reverse_words(example)
print(reversed)
