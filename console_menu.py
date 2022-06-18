################################################################################
#
# Program: Create A Menu For The Console/Terminal/Shell
# 
# Description: Example of how to create a simple menu for the console/terminal/
# shell using Python.  We model a simple ATM machine in this example that allows
# a user to make deposits, withdraw money, print a balance, and quit.
#
# YouTube Lesson: https://www.youtube.com/watch?v=nqx2kMgKRVo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create variables to store the balance, amount to deposit/withdraw, and menu 
# choice selected
balance = 0
amount = 0
choice = ""

# Because we know we want to display the menu repeatedly until the user decides 
# to quit, and because we know we want to display it once, use a while loop 
# with condition True to present the menu.  This will present the menu again 
# and again to the user, and we'll use the 'break' keyword to terminate the 
# loop when the user chooses to quit
while True:
  
  # Present the menu options to the user
  print("1) Deposit")
  print("2) Withdraw")
  print("3) Print Balance")
  print("4) Quit")
  
  # Prompt the user to enter a choice, store the string entered into choice
  choice = input("Enter Choice: ")
  
  # Trims any leading and trailing whitespace characters from the string, so 
  # that if the user enters something like "  3  " with leading and/or 
  # trailing whitespace when trying to enter in the option "3", the string 
  # will be trimmed down to "3" before making the comparisons below (allowing
  # the user to successfully make their selection).
  choice = choice.strip()
   
  # Handle the choice entered with an if-elif-else control structure, first 
  # checking to see if a valid choice from 1-4 was entered using the if and 
  # elif conditions, and then using the else case to handle invalid input.
  if (choice == "1"):
    # In the case of a deposit we prompt the user to enter an amount, convert it
    # to a float value and add it to the balance.
    amount = float(input("Enter Amount: "))
    balance += amount 
  elif (choice == "2"):
    # In the case of a withdraw we again prompt the user to enter an amount, 
    # and convert it to a float, but this time we subtract it from the balance.
    amount = float(input("Enter Amount: "))
    balance -= amount 
  elif (choice == "3"):
    # Output the balance
    print("Balance:", balance)
  elif (choice == "4"):
    # Using break will end the loop right here, control flow will jump to the 
    # next statement after the loop
    break
  # If we have invalid input, inform the user of this and ask them to try again.
  else:
    print("Invalid Option. Please Try Again.")