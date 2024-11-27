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
xcoordinates = 10
ycoordinates = 30

def EntreeJoueur():
    global xcoordinates
    global ycoordinates
    
    ycoordinates += 18
    Toast = input.get()
    if Toast == "":
        create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
        
    else:
        try:
            toast = tmdb.Search().person(query=f'{Toast}')
            print (toast['results'][0]['name'])
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            
        except IndexError:
            print ("Index error, name too long or unrecognized")

boutonclique = 0
def SkipClicked():
    global boutonclique
    boutonclique +=1
    print(boutonclique)
    
def create_text_label(display_text:str, x:int, y:int):
    text = Label(window, text=display_text, font=('Arial', 10, 'bold'))
    text.place(y = y,x = x)


window = Tk()
style = Style()
style.configure('TButton', font =('calibri', 15, 'bold'))

window.title("Movied")
window.minsize(width = 400, height = 400)
window.resizable(False, False)
window.config(padx = 10, pady = 10)
#style.theme_use('clam')

Notice = Label(text = "Find the actor that played in all of those movies", font= ("Helvetica", 12, "bold"), justify=CENTER)
Notice.pack()
Notice2 = Label(text = "From least popular to most popular:", font= ("Helvetica", 9, "bold"), justify=CENTER)
Notice2.pack()




BoutonEntree = Button(window, text = "Enter", command=EntreeJoueur, width=8)
BoutonEntree.place(x = 293, y = 350)

def temp_text(e): #Used to make the inserted text at startup disappear when suer clicks on text box
   input.delete(0,"end")

input = Entry(width=20, font=('courier', 17, 'bold'), foreground='#808080')
input.insert(0, "Actor in common")
input.place(x = 0, y = 350)
input.bind("<FocusIn>", temp_text)












window.mainloop()