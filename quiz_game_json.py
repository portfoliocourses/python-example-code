################################################################################
#
# Program: Quiz Game Using JSON File Data
# 
# Description: Quiz game in Python which uses JSON file data for the multiple
#              choice quiz question and answer data.
#
# YouTube Lesson: https://www.youtube.com/watch?v=V4hOC8RWpjU
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################ 

import json 
import random

# Read the JSON data from a file named quiz.json, the load() function of the
# JSON module will read the data from the file and convert it to a Python list
# of dictionaries.
with open("quiz.json") as f:
    quiz_data = json.load(f)

# Shuffle the quiz questions for randomization
random.shuffle(quiz_data)

# Keep track of the users score and current question
score = 0
question_number = 1

# Question option labels... we could expand this list potentially
letters = ['A', 'B', 'C', 'D']

print("🧠 Welcome to the Multiple-Choice Quiz!\n")

# Loop through each question
for question in quiz_data:

    # Present the question
    print(f"Question {question_number}: {question['question']}") 

    # Present the options with the labels
    options = question['options']
    for i in range(len(options)):
        print(f"  {letters[i]}. {options[i]}") 

    # Accept the user choice, use upper() and strip() to turn lowercase 
    # letters into uppercase and strip prefixed or postfixed whitespace
    # characters for flexibility, e.g. " a" would become "A"
    user_input = input("Your choice (A/B/C/D): ").upper().strip()

    # If the user entered a valid letter...
    if user_input in letters:

        # Find the index of the letter A,B,C,D in the letters list
        index = letters.index(user_input)

        # Then find the text for the option that was selected using the
        # corresponding index
        selected = options[index]

        # If the answer is correct or incorrect, output appropriate feedback
        if selected == question['answer']:
            print("\n✅ Correct!\n")

            # Increment the score if the answer was correct
            score += 1
        else:
            print(f"\n❌ Wrong! Correct answer: {question['answer']}\n")

    # Output error message if the input was not a valid letter
    else:
        print("\n⚠️ Invalid choice. Skipping question.\n")

    # Increment the question number for the next question
    question_number += 1

# Let the user know how they did
print(f"🎯 Quiz complete! You scored {score} out of {len(quiz_data)}")