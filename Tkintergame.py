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



print (Testing.GetReleaseYearOfMovie("Once Upon a Time... in Hollywood"))








