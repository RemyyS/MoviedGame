from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import APIHEADERS

tmdb.API_KEY = f'{APIHEADERS.API}'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = APIHEADERS.HEADERS

def Returns_First_Key_In_Dictionnary(Dictionnaros: dict[str, str]) -> str:  
    for x in Dictionnaros.items():
        aretourner = (x[0])
        return aretourner

def Finding_Person_ID(NameOfPerson: str) -> str:
    recherche = tmdb.Search()
    reponse = recherche.person(query=f"{NameOfPerson}")
    for j in recherche.results:
        return j['id']
    
def Sort_A_Dictionnary_By_Popularity_In_Value_Key(Dictionnaire: dict[str, str]) -> dict[str, str]: #Nom à rallonge, je sais
    return dict(sorted(Dictionnaire.items(), key=lambda item: item[1], reverse=True))

def Sort_Actor_Dictionary_Returns_Most_Popular(Dictionnaire: dict[str, str]) -> str:
    Gribouille = Sort_A_Dictionnary_By_Popularity_In_Value_Key(Dictionnaire)
    for x in Gribouille.items():
        klmnop = True
        while klmnop == True:
            NameOfPersonMostPopular = (x[0])
            klmnop = False
            return NameOfPersonMostPopular

def Returns_Dictionary_Of_Movies_Sorted_By_Popularity_Of_An_Actor_ID(ActorID: str) -> dict[str, str]:
    rangemovienumber = 100
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
    
    DictionnaireDeFilmSorted = Sort_A_Dictionnary_By_Popularity_In_Value_Key(DictionnaireDeFilmASort)
    return DictionnaireDeFilmSorted


tentative = {}
NbPage = 1
def Input_Name_Query_Returns_Actor_Dictionary_Sorted_By_Popularity(NameQuery: str) -> str: 
    #Cursed function, do not modify
    global NbPage
    search = tmdb.Search()
    response = search.person(query=f"{NameQuery}", page = NbPage)
    
    for s in search.results:
        tentative[s['name']] = s['popularity']
    while NbPage < 10:
        NbPage += 1
        Input_Name_Query_Returns_Actor_Dictionary_Sorted_By_Popularity(NameQuery)
    
    tentative2 = Sort_Actor_Dictionary_Returns_Most_Popular(tentative)
    return tentative2

def OrganiserLeDico(Dico):
    for x in Dico:
        print (f"{x} : {Dico[x]}")

def GetReleaseYearOfMovie(MovieName: str) -> str:
    annee = ""
    search = tmdb.Search()
    response = search.movie(query=f"{MovieName}")
    for j in search.results:
        annee = (j['release_date'])
        break
    return annee[0:4]

def JeuCompletFilm(NameOfActor: str) -> dict[str, str]:
    Allez = {}
    Allez = Returns_Dictionary_Of_Movies_Sorted_By_Popularity_Of_An_Actor_ID(Finding_Person_ID(Input_Name_Query_Returns_Actor_Dictionary_Sorted_By_Popularity(NameOfActor)))
    return Allez







"""
#Peut être utile
response = tmdb.Trending(media_type='movie', time_window='week').info()
increasingnumber = 0
for c in response['results']:
    print (response['results'][increasingnumber]['title'])
    increasingnumber +=1
"""

"""""""""
toast = tmdb.People(92614).info()
print (toast['popularity'])
"""""""""

''''''''''''''''
recherche = tmdb.Movies(68726).info()
print(recherche['original_language'])
'''''''''''''''