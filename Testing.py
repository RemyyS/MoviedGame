from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import APIHEADERS
import pyinputplus as pyip
import sys
import testing3
import copy

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
        
        print (f"résultat de fonction FindPersonID : {j['name']}") #Delete this line when full game is out, used for finding the answer.
        return j['id']
    
def DictSortedByPopularityInValue(Dictionnaire: dict[str, str]) -> dict[str, str]: #Nom à rallonge, je sais
    return dict(sorted(Dictionnaire.items(), key=lambda item: item[1], reverse=True))

def MostPopularActorDict(Dictionnaire: dict[str, str]) -> str:
    Gribouille = DictSortedByPopularityInValue(Dictionnaire)
    for x in Gribouille.items():
        NameOfPersonMostPopular = (x[0])
        return NameOfPersonMostPopular

def RequestForDictMoviesActorID(string: str):
    response = tmdb.People(string).movie_credits()
    return response

def DictMoviesOfActorID(ActorID: str) -> dict[str, str]: 
    #Sorted by popularity ASCENDING !!
    rangemovienumber = 80
    NumberToStartMovieList = 0
    response = RequestForDictMoviesActorID(ActorID)
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
    DicoCopiedToReturn = copy.deepcopy(DictionnaireDeFilmSorted)
    DictionnaireDeFilmSorted.clear()
    return DicoCopiedToReturn

NbPage = 1

def RechercheActeurTroisPage(NameQuery: str, NbPage:int = 1): #Hard to explain, but necessary to not create a recursive mess
    Actordict = {}
    search = tmdb.Search()
    response = search.person(query=NameQuery, page = NbPage) 
    
    while NbPage < 3:
        for s in search.results:
            Actordict[s['name']] = s['popularity']
        NbPage += 1
        response = search.person(query=NameQuery, page = NbPage)
    NbPage = 1
    return Actordict





def NameQueryInputActorDictPopularitySorted(NameQuery: str) -> str: 
    
    print(f"Namequery dans la fonction a rallonge : {NameQuery}") #A DELETE
    
    ActorDict2 = RechercheActeurTroisPage(NameQuery)    
    Actordict3 = MostPopularActorDict(ActorDict2)
    
    print(f"retour actor dict 3 : {Actordict3}")
    return Actordict3
    

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
    (Because the most popular list is filled with unknown actors that are extremely niche to certain counrties)
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
            elif finito2['results'][number]['known_for'][0]['popularity'] < 10 and finito2['results'][number]['known_for'][1]['popularity'] < 10 and finito2['results'][number]['known_for'][2]['popularity'] < 10:
                #print(f"finito2['results'][number]['known_for'][0]['title'] has a popularity of finito2['results'][number]['known_for'][0]['popularity'], and every subsequent movie in the "known for" category is below 10 too")
                number +=1
            else:
                DictReturn[finito2['results'][number]['name']] = finito2['results'][number]['known_for'][0]['original_language']
                number +=1
        Startpage +=1
        
    return DictReturn




ListPopularPeople = list(GetPopular().keys())
def JeuCompletFilm() -> dict[str, str]:
    
    
    
    Debugging = random.choice(ListPopularPeople)
    print (f"Après Debugging : {Debugging}")
    DictFinal = {}
    DictFinal = DictMoviesOfActorID(FindPersonID(NameQueryInputActorDictPopularitySorted(str(Debugging))))
    
    Dico2 = {k:DictFinal[k] for k in DictFinal if DictFinal[k] > 8} #Minimum popularity of each movie to be in the list
    
    
    if len(Dico2) < 20: #Number of movies the actor needs to be in to be in the list
        print ("Hit")
        DictFinal.clear()
        Dico2.clear()
        return JeuCompletFilm()
        
    else:
        print ("aaaaaaaaaa")
        print(f"JeuCompletFilm, Dico2 envoyé par la fonction : {Dico2}")
        return Dico2

def ReduceDictToListOfTen(Dict: dict[str, str], SizeOfList:int = 10, NumberOfTopMovies:int = 3) -> list:
    '''Reduce Dictionnary to a List of (SizeOfList, 10 by default)
    appended by the top 3 movies of an actor by default (NumberOfTopMovies), by order ascending, no duplicates'''
    
    #print(f"message de reducedicttolistoften, Dict recu en argument : {Dict}")
    ListDictComplet = list(Dict)
    ListDictMinusThree = [] #Three in variable name by default, but any size put in NumberOfTopMovies
    for x in ListDictComplet:
        ListDictMinusThree.append(x)
    for j in range(NumberOfTopMovies):
        ListDictMinusThree.pop()
    
    number = 1
    FilmReturn = []
    for x in range(SizeOfList):
        FilmReturn.append(ListDictMinusThree[round(len(ListDictMinusThree) / (SizeOfList/number))-1]) #Makes a list of 10 movies, located at the 1/10th, 2/10th, 3/10th etc... length of the movie list, the "10th" being the "SizeOfList" variable
        number +=1
    FinalListAppend = ListDictComplet[:-abs(NumberOfTopMovies)-1:-1]
    FinalListAppend.reverse()
    for x in FinalListAppend:
        FilmReturn.append(x) #Appends the top 3 (or any number in NumberOfTopMovies) movies of the actor to the list of movies
    
    #ListDictMinusThree.clear()
    #ListDictComplet.clear()
    #Dict.clear()
    
    return FilmReturn

def Working_Game(loop: int = 0):
    Dico2 = {}
    Dico2 = JeuCompletFilm()
    print(f"Message de Working_game Dico reçu: {Dico2}")
    DicoListe = ReduceDictToListOfTen(Dico2)
    
    for key in DicoListe:    
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

        if loop == len(DicoListe)-4:
            print ("3 most popular movies :")        
        
        if (loop) == len(DicoListe)-1:
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


def Functest(): # a delete + tard
    yahi = tmdb.Movies(68726).info()
    return yahi['title']

def Tkinterfunctestgetfirstkeyindict(PlayerGuess): # a delete + tard
    toast = tmdb.Search().person(query=f'{PlayerGuess}')
    print (toast['result'](0)['name'])


def GetPopularityOfMovie(MovieName: str) -> str:
    annee = ""
    search = tmdb.Search()
    response = search.movie(query=f"{MovieName}")
    for j in search.results:
        annee = str((j['popularity']))
        if len(annee) == 0:
            return "No data on release date"
        break
    return annee



