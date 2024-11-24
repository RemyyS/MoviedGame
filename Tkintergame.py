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

#toastingos = Testing.JeuCompletFilm() #Working game on terminal
#Testing.Working_Game(toastingos) #Working game on terminal
def EntreeJoueur():
    Toast = input.get()
    if Toast == "":
        SkipClicked()
    else:
        toast = tmdb.Search().person(query=f'{Toast}')
        print (toast['results'][0]['name'])

boutonclique = 0
def SkipClicked():
    global boutonclique
    boutonclique +=1
    print(boutonclique)
    

window = Tk()
window.title("Movied game")
window.minsize(width = 800, height = 800)

nom_du_film = Label(text = Testing.Functest())
nom_du_film.pack()

BoutonEntree = Button(text = "Entree", command=EntreeJoueur)
BoutonEntree.pack(side='bottom')
BoutonSkip = Button(text = "skippos", command=SkipClicked)
BoutonSkip.pack(side= 'bottom')

input = Entry()
input.pack(side = 'bottom')















window.mainloop()