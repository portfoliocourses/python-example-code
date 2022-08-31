################################################################################
#
# Program: Concatenate Two Files
# 
# Description: A program to concatenate (merge) the contents of two files and 
# write the result to a third file.
#
# YouTube Lesson: https://www.youtube.com/watch?v=UaqGPBB-eH4 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Concatenates the contents of the files with filename1 and filename2 into a 
# new file with new_filename
def merge(filename1,filename2,new_filename):

  # Open the files with filenames filename1 and filename2 for reading
  file1 = open(filename1)
  file2 = open(filename2)
  
  # Open the file with filename new_filename for writing
  new_file = open(new_filename, "w")

  # Read the contents of file1 and file2 and store into variables
  file1_contents = file1.read()
  file2_contents = file2.read()
  
  # Write the contents of the first file, followed by hte second file, to 
  # the new file
  new_file.write(file1_contents)
  new_file.write(file2_contents)

  # Close all 3 files as we are done working with them
  file1.close()
  file2.close()
  new_file.close()


# We can call the function like this with hardcoded filenames...
#
# merge("file1.txt", "file2.txt", "newfile.txt")


# Or we could do something like get the filenames of the 3 files from user input
# and use those filenames when calling the function, like this...

filename1 = input("File 1: ")
filename2 = input("File 2: ")
newfile = input("New File: ")

merge(filename1, filename2, newfile)
