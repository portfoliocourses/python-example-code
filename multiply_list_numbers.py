################################################################################
#
# Program: Multiply All Numbers In A List
# 
# Description: Example of how to find the product of all the numbers in a list 
# using Python.  We use two approaches... we create a function to find the 
# product of all the numbers in the list, and we use the numpy function prod()
# to do the same.
#
# YouTube Lesson: https://www.youtube.com/watch?v=xuU2w7n_2mc 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# import the numpy library which includes the prod function to multiply all 
# the numbers in a list.
import numpy 

# returns the product of all the numbers in the list 'numbers'
def list_multiply(numbers):

  # We use product to 'build' the result of multiplying all the numbers in the 
  # list, by multiplying each number by product and storing the result into 
  # product.  We start product off at 1 so that when the first number in the 
  # list is multiplied by product the number itself is the result.
  product = 1

  # have the for loop go through each number in the list
  for number in numbers:
    
    # output the values of product, number, and product*number so we can see 
    # how the loop computes the return value
    print(product,'x',number,'=',product*number)
    
    # multiply the number in the list by product and store the result back into
    # product 
    product = product * number
  
  # return the resulting product
  return product 

# test list should result in 60 as 2 x 3 x 5 x 2 = 60
list1 = [2,3,5,2]

# test out the list_multiply function
print(list_multiply(list1))

# the numpy function prod will give the same result as the list_multiply() function
print(numpy.prod(list1))