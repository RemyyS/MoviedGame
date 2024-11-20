from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import Testing
import APIHEADERS

tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = APIHEADERS.HEADERS

#Testing.OrganiserLeDico(Testing.JeuCompletFilm("Pitt"))


"""
def DeleteActorIfOriginalLanguageNotUS(ActorID):
"""
def GetPopular(nbpage):
    while nbpage < 10:
        finito3 = {}
        url = f"https://api.themoviedb.org/3/person/popular?language=en&page={nbpage}"

        finito = requests.get(url, headers=headers)
        finito2 = json.loads(finito.text)
        nbpage +=1
        finito3.update([finito2])
    return finito3

#print (finito2)
def inputpopulardico(finito3: dict):
    num = 0
    for x in finito3['results']:
        print (finito3['results'][num]['name'])
        num +=1

inputpopulardico(GetPopular(5))
"""
def Check_If_Movie_Is_English(jsonloadiguess: dict):
    num = 3
    
    if jsonloadiguess['results'][0]['known_for'][0]['original_language'] == 'en':
        print (jsonloadiguess['results'][0]['known_for'][0]['title'])
    num += 1

Check_If_Movie_Is_English(finito2)
"""