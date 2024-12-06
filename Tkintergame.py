from tkinter import * 
from tkinter import messagebox
import tmdbsimple as tmdb
import requests
import Testing
import sys
from tkinter.ttk import *
import webstream
import os

tmdb.API_KEY = webstream.APIFINAL
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()
headers = webstream.HEADERS


#toastingos = Testing.JeuCompletFilm() #Working game on terminal
#Testing.Working_Game(toastingos) #Working game on terminal

def main():

    Testing.ListPopularPeople = list(Testing.GetPopular().keys()) #Resets the list
    Testing.Liste3 = Testing.ReduceDictToListOfTen(Testing.JeuCompletFilm()) #Resets the list
    
    global img #Resets the actor photo as last hint
    img = webstream.WebImage(webstream.PictureLink()).get() #Resets the actor photo as last hint
    global imagelab #Resets the actor photo as last hint
    imagelab = Label(window, image=img) #Resets the actor photo as last hint
    
    create_blank_label() #Put the game at starting point
    create_blank_label() #Put the game at starting point
    create_text_label(display_text=Testing.GetListItem()) #Put the game at starting point
    create_genre_label(display_text=Testing.GetGenreItem()) #Put the game at starting point



def restart():
    global labels
    Testing.NumberOfGuess = 0
    for label in labels:
        label.pack_forget()
    labels = []
    main()


def EntreeJoueur(e = 0): #e = 0 is used for event Return, for the user to be able to hit "Enter" on keyboard and it works as if they hit the tkinter button Enter(function input)
    
    
    if Testing.NumberOfGuess == len(Testing.Liste3): #Will trigger when list if exhausted, as a final hint
        create_hint_label()
        
    
    Toast = input.get()
    toast = tmdb.Search().person(query=f'{Toast}')
    
    
    if Toast == "" or Toast == "Who is it ?": #If user doesn't write anything
        pass
    else:
        try: #Try method to solve if user writes gibberish non sense like "bufgefaznjonibfa"
            UserAnswer = toast['results'][0]['name']
        except IndexError:            
            create_text_label(display_text=Testing.GetListItem())
            create_genre_label(display_text=Testing.GetGenreItem())

            CMDoutput.config(text=f"No name found linked to that input")
    try: #Catch the UnboundLocalError
        if Toast == "" or Toast == "Who is it ?": #If the user didn't write anything :
            create_text_label(display_text=Testing.GetListItem())
            create_genre_label(display_text=Testing.GetGenreItem())

            CMDoutput.config(text=f"")
        elif UserAnswer != Testing.NameToGuess: #If the user got it wrong :
            CMDoutput.config(text=f"No, this isn't {UserAnswer}")
            create_text_label(display_text=Testing.GetListItem())
            create_genre_label(display_text=Testing.GetGenreItem())

        else:                            
            if UserAnswer == Testing.NameToGuess: #If the user got it right
                CMDoutput.config(text=f"Congratulations ! It is {UserAnswer} !")
                
        
    
    except UnboundLocalError: #Try method to catch the previous IndexError for the previous block, writing in the previous IndexError except method to set the UserAnswer string to a default value is catastrophic in future damages
        pass
    
    if Testing.NumberOfGuess > len(Testing.Liste3)+1:
            try_again = messagebox.askyesno(title="Try again ?",  message=f"The answer was {Testing.NameToGuess} ! \n Would you like to play again ? (It takes a few seconds to load)" )
            if try_again:
                restart()
            else:
                sys.exit()

    
def create_text_label(display_text:str): #X and Y args used for .place() method
    global labels #Used for restarting the game
    textrecursive = Label(window, text=display_text, font=('Arial', 10, 'bold'), justify='center', background='light grey')
    labels.append(textrecursive)
    textrecursive.pack(side=TOP)
    
    #text.place(y = y,x = x)

def create_genre_label(display_text:str): #X and Y args used for .place() method
    global labels #Used for restarting the game
    textgenre = Label(window, text=display_text, justify='center')
    labels.append(textgenre)
    textgenre.pack(side=TOP)
    create_blank_label()

def create_blank_label():
    global labels #Used for restarting the game
    blank = Label(window, text = "", background='#380000')
    labels.append(blank)
    blank.pack(side=TOP)

def create_hint_label():
    global labels #Used for restarting the game
    hint = Label(window, text = "Picture hint and last try !", background='light green')
    labels.append(hint)
    
    #img = webstream.WebImage(webstream.link).get() 
    #imagelab = Label(window, image=img) 
    imagelab.pack(side=TOP)
    labels.append(imagelab)
    
    hint.pack(side=TOP)

def temp_text(e): #Used to make the inserted text at startup disappear when user clicks on text box
   input.delete(0,"end")


    
window = Tk()
style = Style()
style.configure('TButton', font =('calibri', 15, 'bold'))
labels = []

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
Notice2 = Label(text = "Based on the movies they were in, popularity ascending", font= ("courier", 12, "underline", "bold"), justify=CENTER, anchor=N, borderwidth=0, relief="flat", width= 0, background='#380000', foreground='light grey')
Notice2.pack()
CMDoutput = Label(text= "", font= ("Helvetica", 12, "bold"), background='light blue')






BoutonEntree = Button(window, text = "Enter", command=EntreeJoueur, width=8)
BoutonEntree.pack(side=BOTTOM)



input = Entry(width=20, font=('courier', 17, 'bold'), foreground='#808080')
input.insert(0, "Who is it ?")
input.pack(side=BOTTOM)
input.bind("<FocusIn>", temp_text)
input.bind("<Return>", EntreeJoueur) #Used to make the user hit "Enter" on keyboard to validate their input instead of clicking




CMDoutput.pack(side='bottom')



main()



window.mainloop()



