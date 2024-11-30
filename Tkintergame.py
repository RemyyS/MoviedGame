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
import webstream
from PIL import ImageTk, Image
import os

tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()
headers = APIHEADERS.HEADERS


#toastingos = Testing.JeuCompletFilm() #Working game on terminal
#Testing.Working_Game(toastingos) #Working game on terminal

xcoordinates = 5 #used for deprecated .place method
ycoordinates = 20 #used for deprecated .place method

import sys
import os

def restart_program():
    """Restarts the current program.
    Note: this function does not return."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
""" 
if __name__ == "__main__":
    answer = raw_input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program() 
"""

def EntreeJoueur(e = 0): #e = 0 is used for event Return, for the user to be able to hit "Enter" on keyboard and it works as if they hit the tkinter button Enter(function input)
    
    global xcoordinates #Get coordinates to print new labels for the .place method
    global ycoordinates #Get coordinates to print new labels for the .place method
    ycoordinates += 18 #deprecated .place method to place movies appearing
    
    if Testing.NumberOfGuess > len(Testing.Liste3): #Will trigger when list if exhausted, as a final hint
        print('hit')
        imagelab.pack(side=TOP)

    Toast = input.get()
    toast = tmdb.Search().person(query=f'{Toast}')
    
    
    if Toast == "" or Toast == "Who is it ?": #If user doesn't write anything
        pass
    else:
        try: #Try method to solve if user writes gibberish non sense like "bufgefaznjonibfa"
            UserAnswer = toast['results'][0]['name']
        except IndexError:            
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            create_genre_label(display_text=Testing.GetGenreItem(), x=xcoordinates, y=ycoordinates)

            CMDoutput.config(text=f"No name found linked to that input")
    try: #Catch the UnboundLocalError
        if Toast == "" or Toast == "Who is it ?": #If the user didn't write anything :
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            create_genre_label(display_text=Testing.GetGenreItem(), x=xcoordinates, y=ycoordinates)

            CMDoutput.config(text=f"")
        elif UserAnswer != Testing.NameToGuess: #If the user got it wrong :
            CMDoutput.config(text=f"No, this isn't {UserAnswer}")
            create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
            create_genre_label(display_text=Testing.GetGenreItem(), x=xcoordinates, y=ycoordinates)

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
    
def create_text_label(display_text:str, x:int, y:int): #X and Y args used for .place() method
    textrecursive = Label(window, text=display_text, font=('Arial', 10, 'bold'), justify='center')
    textrecursive.pack(side=TOP)
    
    #text.place(y = y,x = x)

def create_genre_label(display_text:str, x:int, y:int): #X and Y args used for .place() method
    textgenre = Label(window, text=display_text, justify='center')
    textgenre.pack(side=TOP)
    create_blank_label()

def create_blank_label():
    blank = Label(window, text = "", background='#380000')
    blank.pack(side=TOP)


window = Tk()
style = Style()
style.configure('TButton', font =('calibri', 15, 'bold'))


""" 
image = Image.open('photo_cinema.jpg') #Used for background pictures, see webstream.py
bg_image = ImageTk.PhotoImage(image) #Used for background pictures, see webstream.py
CanvasTest = Canvas(window, width=bg_image.width(), height=bg_image.height()) #Used for background pictures, see webstream.py
CanvasTest.place(x=0, y=0) #Used for background pictures, see webstream.py
CanvasTest.create_image(0, 0, image=bg_image, anchor='nw') #Used for background pictures, see webstream.py
"""

window.title("Movied")
window.minsize(width = 600, height = 850)
window.configure(background='#380000')
window.config(padx = 0, pady = 0)
#style.theme_use('clam')

Notice = Label(text = "Find the actor", font= ("courier", 25, "bold"), justify=CENTER, anchor=S, borderwidth=0, relief="flat", compound=CENTER, width=0, background='#380000', foreground='white')
Notice.pack()
Notice2 = Label(text = "Based on the movies they were in, popularity ascending", font= ("courier", 12, "underline"), justify=CENTER, anchor=N, borderwidth=0, relief="flat", width= 0, background='#380000', foreground='light grey')
Notice2.pack()
CMDoutput = Label(text= "test", font= ("Helvetica", 12, "bold"), background='#380000')



img = webstream.WebImage(webstream.link).get() 
imagelab = Label(window, image=img) 




BoutonEntree = Button(window, text = "Enter", command=EntreeJoueur, width=8)
BoutonEntree.pack(side=BOTTOM)

def temp_text(e): #Used to make the inserted text at startup disappear when user clicks on text box
   input.delete(0,"end")

input = Entry(width=20, font=('courier', 17, 'bold'), foreground='#808080')
input.insert(0, "Who is it ?")
input.pack(side=BOTTOM)
input.bind("<FocusIn>", temp_text)
input.bind("<Return>", EntreeJoueur) #Used to make the user hit "Enter" on keyboard to validate their input instead of clicking



create_blank_label()
create_blank_label()
create_text_label(display_text=Testing.GetListItem(), x=xcoordinates, y=ycoordinates)
create_genre_label(display_text=Testing.GetGenreItem(), x=xcoordinates, y=ycoordinates)



CMDoutput.pack(side='bottom')
window.mainloop()