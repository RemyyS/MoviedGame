from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import APIHEADERS
import pyinputplus as pyip
import sys

tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = APIHEADERS.HEADERS

def FirstKeyInDict(Dictionnaros: dict[str, str]) -> str:  
    for x in Dictionnaros.items():
        Toreturn = (x[0])
        return Toreturn

def FindPersonID(NameOfPerson: str) -> str:
    recherche = tmdb.Search()
    reponse = recherche.person(query=f"{NameOfPerson}")
    for j in recherche.results:
        global NameToGuess
        NameToGuess = (j['name'])
        print (j['name']) #Delete this line when full game is out, used for finding the answer.
        return j['id']
    
def DictSortedByPopularityInValue(Dictionnaire: dict[str, str]) -> dict[str, str]: #Nom à rallonge, je sais
    return dict(sorted(Dictionnaire.items(), key=lambda item: item[1], reverse=True))

def MostPopularActorDict(Dictionnaire: dict[str, str]) -> str:
    Gribouille = DictSortedByPopularityInValue(Dictionnaire)
    for x in Gribouille.items():
        klmnop = True
        while klmnop == True:
            NameOfPersonMostPopular = (x[0])
            klmnop = False
            return NameOfPersonMostPopular

def DictMoviesOfActorID(ActorID: str) -> dict[str, str]: 
    #Sorted by popularity ASCENDING !!
    rangemovienumber = 50
    NumberToStartMovieList = 0
    response = tmdb.People(ActorID).movie_credits()
    DictionnaireDeFilmASort = {}
    DictionnaireDeFilmSorted = {}
    try:
        for t in range(rangemovienumber):
            DictionnaireDeFilmASort[response['cast'][NumberToStartMovieList]['title']] = response['cast'][NumberToStartMovieList]['popularity']
            NumberToStartMovieList +=1
    except IndexError: #Trigger si "rangemovienumber" dépasse l'index du nombre de film (s'il y a + d'index que de films dans lequel l'acteur a joué)
        pass
        #print (f"The actor has played in {NumberToStartMovieList -1} movies in his entire career, end of the list")
    
    DictionnaireDeFilmSorted = dict(sorted(DictionnaireDeFilmASort.items(), key=lambda item: item[1], reverse=False)) #Sort by popularity ASCENDING, key[0] is the LEAST popular movie
    return DictionnaireDeFilmSorted


Actordict = {}
NbPage = 1
def NameQueryInputActorDictPopularitySorted(NameQuery: str) -> str: 
    #Cursed function, do not modify
    global NbPage
    search = tmdb.Search()
    response = search.person(query=f"{NameQuery}", page = NbPage)
    
    for s in search.results:
        Actordict[s['name']] = s['popularity']
    while NbPage < 10:
        NbPage += 1
        NameQueryInputActorDictPopularitySorted(NameQuery)
    
    Actordict2 = MostPopularActorDict(Actordict)
    return Actordict2

def OrganiserLeDico(Dico):
    for x in Dico:
        print (f"{x} : {Dico[x]}")

def GetReleaseYearOfMovie(MovieName: str) -> str:
    annee = ""
    search = tmdb.Search()
    response = search.movie(query=f"{MovieName}")
    for j in search.results:
        annee = (j['release_date'])
        if len(annee) == 0:
            return "No data on release date"
        break
    
    
    return annee[0:4]



def GetPopular(Startpage: int = 1, Endpage: int = 15)-> dict[str, str]:
    '''
    Returns dictionnary of actors in the "most popular" tab,
    from page 1 to 15 by default.
    The dictionnary includes their 'names' as keys, and original langage of their most popular movie as 'values'
    Does not add any actor to the return dictionary that doesn't have a 'en' (english as primary spoken language) movie as their most popular movie.
    (Because the most popular list is filled with unknown actors that are extremely niche in certain counrties)
    '''
    
    DictReturn ={}
    while Startpage < Endpage:
        url = f"https://api.themoviedb.org/3/person/popular?language=en&page={Startpage}"

        finito = requests.get(url, headers=headers)
        finito2 = json.loads(finito.text)
        
        number = 0
        for x in finito2['results']:
            if finito2['results'][number]['known_for'][0]['original_language'] != 'en':
                #print(f"{finito2['results'][number]['name']} is not english but {finito2['results'][number]['known_for'][0]['original_language']}")
                number +=1
            else:
                DictReturn[finito2['results'][number]['name']] = finito2['results'][number]['known_for'][0]['original_language']
                number +=1
        Startpage +=1
        
    return DictReturn


def JeuCompletFilm() -> dict[str, str]:
    
    Allez = DictMoviesOfActorID(FindPersonID(NameQueryInputActorDictPopularitySorted(str(random.choice(list(GetPopular().keys()))))))
    return Allez


def Working_Game(DicoComplet: dict[str, str], loop: int = 0):
    
    for key in DicoComplet.keys():    
        print(f'{key}, released in : {GetReleaseYearOfMovie(key)}')
        
        PlayerGuess = pyip.inputStr("Enter name of the actor that played in all of those movies : >")
        recherche = tmdb.Search().person(query=f'{PlayerGuess}')
        try:
            if recherche['results'][0]['name'] == NameToGuess:
                print(f'Bien joue la team')
                sys.exit()
            
            else:
                print(f"Non, ce n'est pas {recherche['results'][0]['name']}")
        except IndexError:
            print('No results for this name, try again')
            loop +=1
            continue

        if (loop) == len(DicoComplet)-1:
            print("fin du jeu")
            
            sys.exit()
        loop +=1

"""
#Peut être utile
response = tmdb.Trending(media_type='movie', time_window='week').info()
increasingnumber = 0
for c in response['results']:
    print (response['results'][increasingnumber]['title'])
    increasingnumber +=1
"""


def Functest():
    yahi = tmdb.Movies(68726).info()
    return yahi['title']

def Tkinterfunctestgetfirstkeyindict(PlayerGuess):
    toast = tmdb.Search().person(query=f'{PlayerGuess}')
    print (toast['result'](0)['name'])
