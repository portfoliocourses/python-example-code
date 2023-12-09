################################################################################
#
# Program: Find The Longest Common Prefix In A List Of Strings
# 
# Description: Program to find the longest common prefix in a list of strings
# using Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=MbAQiZLWnXU
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Returns string of the longest common prefix in the list of strings
def longest_prefix(strings):

    # Stores the longest common prefix found so far, initially empty/blank
    max_prefix = ""

    # Check if strings list is empty (not strings is True if so) and return 
    # the empty max_prefix string if so
    if not strings:
        return max_prefix 

    # Find the shortest string (min_string) in the strings list using the 
    # built-in min() function, as the longest common prefix cannot possibly
    # be longer than this string by definition (otherwise it would not be 
    # a common prefix).  The keyword argument key=len will have min() use 
    # the built-in len() length function to determine the "minimum string",
    # i.e. the minimum string returned by min() will be the one with the 
    # shortest length.
    min_string = min(strings, key=len) 

    # The counter variable i goes from 0 up until but not including the 
    # length of the min_string with each iteration of the loop.  We use
    # this counter variable to check if increasingly longer prefixes of 
    # the min_string are prefixes of all strings, where min_string[:i+1]
    # gives us the prefix of the min_string from index 0 up until but 
    # not including the index i+1.  So if the min_string is ape:
    # 
    # - In first loop iteration min_string[:i+1] is "a"
    # - In second loop iteration min_string[:i+1] is "ap"
    # - In third loop iteration min_string[:i+1] is "ape"
    #
    # We then use the list comprehension to see if each string in the list
    # strings starts with this prefix of the min_string (the startswith 
    # method will return True if the string does, and False otherwise).  The
    # built-in all() method will check the list of resulting True/False 
    # items because if ALL the items are True that means ALL the strings in the 
    # list have this prefix of the min_string as a prefix.  If that is the 
    # case the all() method will return True, and in that case we update the 
    # max_prefix string as we have found a new longer common prefix.
    #
    # We continue to check if longer prefixes of the min_string are common to
    # all strings and updating max_prefix if so, until either we reach the end
    # of min_string OR we find a prefix of min_string that is NOT a prefix of 
    # all the other strings.  max_prefix will contain the longest common prefix
    # and so we return that string.
    #
    for i in range(0, len(min_string)):
        if all([s.startswith(min_string[:i+1]) for s in strings]):
            max_prefix = min_string[:i+1]
        else:
            break
 
    return max_prefix

# Test list of strings with "ap" is the longest common prefix
string_list = ["apply", "application", "ape", "apples", "append"]

# Test the function which should return "ap"
print(longest_prefix(string_list))