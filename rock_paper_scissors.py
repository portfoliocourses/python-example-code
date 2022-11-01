################################################################################
#
# Program: Rock Paper Scissors Game
#
# Description: An implementation of the rock paper scissors game in Python.
# See the Wikipedia article: https://en.wikipedia.org/wiki/Rock_paper_scissors
#
# YouTube Lesson: https://www.youtube.com/watch?v=bEGHcXUivls 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Rock Paper Scissors Rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#
# All other possibilities are a tie.  We'll have the player pick a throw, and
# we'll randomly select an "AI throw" for the other player from the three
# possible throws.  We'll repeatedly allow the player to play the game until
# they quit.
#

# Random module choice() function will be used to randomly select the AI throw
import random


# Use condition True to have the while loop continue indefinitely until the
# player decides to quit
while True:

    # Present the menu of possible throws to the player and prompt them to enter
    # a throw using input().  The input() function will pause to allow the
    # player to enter a string and it will return that string that the player
    # enters.  We expect the player to enter 1, 2 or 3, so we use int() to
    # convert the return value of input() to an int value and we store it into
    # selection.  We output "\n" to have a couple newlines to vertically
    # separate the menu from any content that came before it on the terminal.
    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    selection = int(input("Enter Throw: "))

    # Next we set player_throw to either "Rock", "Paper" or "Scissors" based on
    # the choice the user has made.  Technically we could have asked the player
    # to enter these strings directly but a menu with numbers may be simpler
    # for the user.
    if (selection == 1):
        player_throw = "Rock"
    elif (selection == 2):
        player_throw = "Paper"
    else:
        player_throw = "Scissors"

    # Output the player throw
    print("\n")
    print("Player throws", player_throw)

    # Randomly select the AI throw from the list of possible throws using the
    # choice() function of the random module.  The choice() function will
    # return one of the throws list elements randomly and we'll store that
    # throw into ai_throw.
    throws = ["Rock", "Paper", "Scissors"]
    ai_throw = random.choice(throws)

    # Output the ai_throw
    print("AI throws", ai_throw)

    # If the player throw and AI throw are the same, it's a tie game.  Otherwise
    # we need to look at the other possibilities to see who won.  In the outter
    # if statement we check for the possibilities that the player throw is
    # rock, paper, or scissors.  Then we use a nested if-statement in each
    # of these outer if-statement branches to check for the possible AI
    # throws (and there are only two possible throws because we've already
    # handled the possibility the two throws are the same).  We output the
    # correct result of the game according to the rules in all cases.
    if (player_throw == ai_throw):
        print("Tie Game!")
    elif (player_throw == "Rock"):
        if (ai_throw == "Paper"):
            print("AI Wins!")
        elif (ai_throw == "Scissors"):
            print("Player Wins!")
    elif (player_throw == "Paper"):
        if (ai_throw == "Scissors"):
            print("AI Wins!")
        elif (ai_throw == "Rock"):
            print("Player Wins!")
    elif (player_throw == "Scissors"):
        if (ai_throw == "Rock"):
            print("AI Wins!")
        elif (ai_throw == "Paper"):
            print("Player Wins!")

    # Output a menu that will allow the player to quit the game.  As before we
    # store the choice the player enters into the select variable as an int
    # value.
    print("\n")
    print("1) Play Again")
    print("2) Quit")
    selection = int(input("Enter Choice: "))

    # If the player entered 2 they wish to quit the game, and we use break
    # to stop the execution of the loop.
    if (selection == 2):
        break