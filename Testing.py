from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random

tmdb.API_KEY = '5046bd40ead6143ad0243a87775b1ff1'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MDQ2YmQ0MGVhZDYxNDNhZDAyNDNhODc3NzViMWZmMSIsIm5iZiI6MTczMTY0MzgwOS43MDIyNTA3LCJzdWIiOiI2NzM2YzNmNzcxZWY2Njk3OGNmYWZiNGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.XjqyInYwlKE8VzRX_SWART2QtHU09gDfgzx7jfaPkKs"
}

"""
search = tmdb.Search()
response = search.person(query="Cruise")
tentative = {}

for s in search.results:
    tentative[s['name']] = s['popularity']

print (tentative)

tentativesorted = dict(sorted(tentative.items(), key=lambda item: item[1], reverse=True))

print(tentativesorted)    
for x in tentativesorted.items():
    print (x[0]) #Va print le premier nom du dico
    break    

"""
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
    rangemovienumber = 10
    NumberToStartMovieList = 0
    response = tmdb.People(ActorID).movie_credits()
    DictionnaireDeFilmASort = {}
    DictionnaireDeFilmSorted = {}
    try:
        for t in range(rangemovienumber):
            DictionnaireDeFilmASort[response['cast'][NumberToStartMovieList]['title']] = response['cast'][NumberToStartMovieList]['popularity']
            NumberToStartMovieList +=1
    except IndexError: #Trigger si "rangemovienumber" dépasse l'index du nombre de film (s'il y a + d'index que de films dans lequel l'acteur a joué)
        print (f"The actor has played in {NumberToStartMovieList -1} movies in his entire career, end of the list")
    
    DictionnaireDeFilmSorted = Sort_A_Dictionnary_By_Popularity_In_Value_Key(DictionnaireDeFilmASort)
    return DictionnaireDeFilmSorted


"""
rangemovienumber = 100
NumberToStartMovieList = 0
response = tmdb.People(103).movie_credits()
DictionnaireDeFilmASort = {}
try:
    for t in range(rangemovienumber):
        
        #print (response['cast'][NumberToStartMovieList]['title'], ":", response['cast'][NumberToStartMovieList]['popularity'])
        DictionnaireDeFilmASort[response['cast'][NumberToStartMovieList]['title']] = response['cast'][NumberToStartMovieList]['popularity']
        NumberToStartMovieList +=1
except IndexError: #Trigger si "rangemovienumber" dépasse l'index du nombre de film (s'il y a + d'index que de films dans lequel l'acteur a joué)
    print (f"The actor has played in {NumberToStartMovieList -1} movies in his career")
"""



