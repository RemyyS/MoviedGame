from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import Testing
import APIHEADERS
import pyinputplus as pyip
import sys
tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = APIHEADERS.HEADERS

#Testing.OrganiserLeDico(Testing.JeuCompletFilm("Pitt"))


Flopping = (Testing.JeuCompletFilm())

print(Testing.NameToGuess) #str
print(Flopping)

loop = 0
keyloop = 5 #Démarre le jeu au 5ème (6ème en vrai) key du dictionnaire des films (les 5 moins populaires sont généralement trop niches)
#transformer en liste pouyr mieux itérer lmes loops je suppose
for key in Flopping.keys():
    
    
    
    Skipunfilmtoutlesfilms = 0
    print(f'{key}, released in : {Testing.GetReleaseYearOfMovie(key)}')
    
    PlayerGuess = pyip.inputStr("Enter name of the actor that played in all of those movies : >")
    recherche = tmdb.Search().person(query=f'{PlayerGuess}')
    try:
        if recherche['results'][0]['name'] == Testing.NameToGuess:
            print(f'Bien joue la team')
            sys.exit()
        else:
            print(f"Non, ce n'est pas {recherche['results'][0]['name']}")
    except IndexError:
        print('No results for this name, try again')
        loop +=1
        continue
    if str(loop) == len(Flopping) -1:
        print("fin du jeu")
        sys.exit()
    
    loop +=1
    keyloop +=2