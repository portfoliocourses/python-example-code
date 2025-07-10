################################################################################
#
# Program: Slot Machine Game
# 
# Description: A simple and fun slot machine game in Python.
#
# YouTube Lesson: https://www.youtube.com/watch?v=d_LUoX8w8Hk
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

import random

# symbols for the slot machine spins
symbols = ["🍒", "🍋", "🔔", "💎", "7", "🍀"]

print("🎰 Welcome to the Slot Machine! 🎰")

# Continue the game until the player declines to continue
while True:

    # choices() returns a list with 3 random items from the symbols list, BUT
    # we can have repeats, e.g. 2 lemons 1 diamond, 3 cherries, etc.
    spin = random.choices(symbols, k=3)

    # Output the results of the spin
    print("\nSpinning...")
    print(f"\n| {spin[0]} | {spin[1]} | {spin[2]} |")

    # Analyze the results (3 matches, 2 matches, none) and ouput a suitable
    # message to the player
    if spin[0] == spin[1] == spin[2]:
        print("\n🎉 JACKPOT! All three match!")
    elif spin[0] == spin[1] or spin[0] == spin[2] or spin[1] == spin[2]:
        print("\n✨ Two symbols match! Not bad!")
    else:
        print("\n🙁 No match. Try again!")

    # Prompt the player to check if they want to continue.  We use strip() to 
    # remove any trailing or leading whitespace, and we use lower() to set all
    # letters in the string to lowercase.  This accounts for the player entering 
    # in leading or trailing space characters, or entering an uppercase Y.
    #
    # We use break to stop the loop if the player input was anything other 
    # than 'y'...
    #
    choice = input("\nPlay again? (y/n): ").strip().lower()
    if choice != 'y':
        print("\nThanks for playing! 🎲")
        break