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
import time
from tkinter.ttk import *

tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()
headers = APIHEADERS.HEADERS

# --url 'https://api.themoviedb.org/3/movie/550/images?language=en-US&include_image_language=en,null'
# https://image.tmdb.org/t/p/original/c0HNhjChGybnHa4eoLyqO4dDu1j.jpg URL FOR PICTURES

# images = tmdb.People(Testing.IDActor).images()
#for image in images['profiles']:
#    print(image)

#toastingos = Testing.JeuCompletFilm() #Working game on terminal
#Testing.Working_Game(toastingos) #Working game on terminal



xcoordinates = 5
ycoordinates = 20

def EntreeJoueur():
    global xcoordinates #Get coordinates to print new labels
    global ycoordinates
    ycoordinates += 18
    
    Toast = input.get()
    toast = tmdb.Search().person(query=f'{Toast}')
    
    if Toast == "" or Toast == "Actor in common": #If user doesn't write anything
        pass
    else:
        try: #Try method to solve if user writes gibberish non sense like "bufgefaznjonibfa"
            UserAnswer = toast['results'][0]['name']
        except IndexError:            
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            CMDoutput.config(text=f"No name found linked to that input")
    try: 
        if Toast == "" or Toast == "Actor in common": #If the user didn't write anything :
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            CMDoutput.config(text=f"")
        elif UserAnswer != Testing.NameToGuess: #If the user got it wrong :
            CMDoutput.config(text=f"No, this isn't {UserAnswer}")
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
        else:                            
            if UserAnswer == Testing.NameToGuess: #If the user got it right
                CMDoutput.config(text=f"Congratulations ! It is {UserAnswer} !")
                
                            
    except UnboundLocalError: #Try method to catch the previous IndexError for the previous block, writing in the previous IndexError except method to set the UserAnswer string to a default value is catastrophic in future damages
        pass

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

Notice = Label(text = "From least popular to most popular:", font= ("Helvetica", 12, "bold"), justify=CENTER)
Notice.pack()
#Notice2 = Label(text = "From least popular to most popular:", font= ("Helvetica", 9, "bold"), justify=CENTER)
#Notice2.pack()
CMDoutput = Label(text= "test", font= ("Helvetica", 12, "bold"))
CMDoutput.place(x = 5, y = 325)



BoutonEntree = Button(window, text = "Enter", command=EntreeJoueur, width=8)
BoutonEntree.place(x = 293, y = 350)

def temp_text(e): #Used to make the inserted text at startup disappear when user clicks on text box
   input.delete(0,"end")

input = Entry(width=20, font=('courier', 17, 'bold'), foreground='#808080')
input.insert(0, "Actor in common")
input.place(x = 0, y = 350)
input.bind("<FocusIn>", temp_text)












window.mainloop()