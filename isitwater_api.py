################################################################################
#
# Program: Check If A Location Is On Land Or Water
#
# Description: Example of using the IsItWater API to check if a coordinate is 
# on land or water with Python. 
#
# YouTube Lesson: https://www.youtube.com/watch?v=H32xQz8r8yA
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# The api is used according to the documentation available here: 
# https://isitwater.com/

# The requests module is used to make the http request to the API
import requests

# An api key is required, this API key will be disabled so you must obtain 
# your own by registering using the above URL.
api_key = "fb7a7088ccmsha0a1556ab1f0ac9p19678fjsn9151e331d519"

# This is the api "endpoint" where the request must be made
url = "https://isitwater-com.p.rapidapi.com/"

# We include the API key in the request query parameters, along with a 
# latitude and longitude for a geographic coordinate
params = {"rapidapi-key" : api_key,
          "latitude" : "19.241244",
          "longitude" : "72.888650"}

# Makes the get request with the endpoint and parameters and returns a response
# object.  The response will be made up of JSON data.
response = requests.get(url, params)

# We use the .json() method to obtain a Python dictionary of the response data.
data = response.json()

# Output the response data.  The key water will be set to True if the coordinate
# is on water, and false if the coordinate is on land.
print(data)