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
from tkinter.ttk import *

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
style = Style()
style.configure('TButton', font =('calibri', 20, 'bold'))

window.title("Movied game")
window.minsize(width = 800, height = 800)

#style.theme_use('clam')

Notice = Label(text = "Find the actor that played in all of those movies : ")
Notice.pack()
nom_du_film = Label(text = Testing.Functest())
nom_du_film.pack()



BoutonEntree = Button(window, text = "Entree", command=EntreeJoueur)
BoutonEntree.pack(side='bottom')
BoutonSkip = Button(text = "skippos", command=SkipClicked)
BoutonSkip.pack(side= 'bottom')

input = Entry()
input.pack(side = 'bottom')















window.mainloop()