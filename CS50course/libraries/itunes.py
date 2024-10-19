#This is the library that lets you do requests to the internet like searches and other stuff
import requests
#This library for the time being is just serving as a way to write parameters before running the programs
import sys
#This library helps me to read json files (JavaScript Object Notation)
#more specifically 
#The python sys module contains methods and variables for modifying
#  many elements of the Python Runtime Environment. It allows us to access 
# parameters and functionalities specific to the system.
import json

if len(sys.argv) != 2:
    sys.exit()
#This line serves to get the info from the URL which this time is searching for the name of a band I specified b/f
response  = requests.get("https://itunes.apple.com/search?entity=song&limit=30&term="  + sys.argv[1])
#This is printing the info in a json format
#json.dumps helps me to make the file more readable and the indent is just there to specify how many blank spaces of indentation I want
#print(json.dumps(response.json(), indent = 2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])