################################################################################
#
# Program: nonlocal Keyword Example
#
# Description: Example of using the nonlocal keyword in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=27S2qRdH2rM
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

def outer():
  
  # This variable is in the "enclosing scope" of the inner function below
  enclosing_scope_variable = 10

  def inner(): 

    # In order to give the inner function access to the enclosing_scope_variable
    # we must use nonlocal like this.  Try commenting out the below line to see
    # the difference.  If we do not do this, instead a new variable local to 
    # the inner function called 'enclosing_scope_variable' will be created,
    # and it will be different than the enclosing_scope_variable of the outer
    # function.  And so in that case assigning 20 to enclosing_scope_variable
    # would not change THAT variable's value (the variable in the enclosing 
    # scope of inner, which is the local scope of outer).  Instead because 
    # we use nonlocal, inner will be given the same enclosing_scope_variable
    # as in the enclosing scope, and we DO change that variable's value!
    # 
    nonlocal enclosing_scope_variable
    enclosing_scope_variable = 20
    print("inner:", enclosing_scope_variable)
 
  inner()
  print("outer:", enclosing_scope_variable)

outer()
