################################################################################
#
# Program: Dad Joke Generator
# 
# Description: Program to tell dad jokes using Python and the 
#              icanhazdadjokes.com API.
#
# YouTube Lesson: https://www.youtube.com/watch?v=09XUBRjOD2A
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Used to make HTTP requests
import requests

# Request header for the request, ensures we get back JSON data in the response
request_headers = {
    "Accept" : "application/json"
}
 
# Continue to tell dad jokes until the user decides to stop
while True:

    # Makes the request to the API, using a GET verb and the request header
    response = requests.get("https://icanhazdadjoke.com",
                            headers=request_headers)

    # If the response is not OK, exit using break to stop the loop
    if response.status_code != 200:
        print("\nSorry, I ran out of jokes. Dad brain!")
        break

    # Otherwise output the joke by getting the response body using .json(),
    # getting the value at the key 'joke'
    print(f"\n{response.json()['joke']}")  

    # Exit if the user decides to do so, again using break to stop the loop.
    # We use lower() to make all letters in the string lowercase just in 
    # case the user enters in 'N' instead of 'n'.
    user_input = input("\nAnother joke? (y/n): ").lower()
    if user_input == 'n':
        print("\nLater, alligator!")
        break 