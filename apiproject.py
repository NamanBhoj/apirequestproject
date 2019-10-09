import requests
from random import choice 
import pyfiglet

header = pyfiglet.figlet_format("NAMAN SEARCHED FOR JOKES")
print(header)

welcome = input("What are you looking for?
 ")

url = "https://icanhazdadjoke.com/search" #/search because we want an applicaiton where user can lookout for jokes with the help of a keyword 

response = requests.get(url, headers = {"Accept": "application/json"}, params = {"term":welcome}).json()
#params does the same thing as adding a query string to the url.
#print(response)

#counting the number of jokes related to the query 

numjokes = response["total_jokes"]
results = response["results"]
if numjokes>1 :
    print("There are numerous jokes. Here is one.")
    print(choice(results)["joke"])
elif numjokes == 1 :

    print("There is only one joke")
    print(results[0]["joke"])
else: 
    print("There are no jokes")   
