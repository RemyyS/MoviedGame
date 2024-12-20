from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
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
NameToGuess = ''
def FirstKeyInDict(Dictionnaros: dict[str, str]) -> str:  
    for x in Dictionnaros.items():
        Toreturn = (x[0])
        return Toreturn

def FindPersonID(NameOfPerson: str) -> str:
    recherche = tmdb.Search()
    reponse = recherche.person(query=f"{NameOfPerson}")
    for j in recherche.results:
        try:
            global NameToGuess
            NameToGuess = (j['name']) #Where the answer gets taken from
            global IDActor
            IDActor = (j['id']) #Where the ID comes from for actor profile/picture
            #print (f"résultat de fonction FindPersonID : {j['name']}") #Delete this line when full game is out, used for finding the answer.
            
            return j['id']
        except IndexError:
            print ("Index error, name too long or unrecognized")
    
def DictSortedByPopularityInValue(Dictionnaire: dict[str, str]) -> dict[str, str]: #Sorts a Dictionnary by their VALUES, not KEYS !!
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

def RechercheActeurTroisPage(NameQuery: str, NbPage:int = 1): #Necessary to not create a recursive mess, relating tot he API call
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
    '''
    Input Name Query (of an actor), 
    returns a dict of actors that matches the query,
    sorted by popularity.
    '''
    ActorDict2 = RechercheActeurTroisPage(NameQuery)    
    Actordict3 = MostPopularActorDict(ActorDict2)
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



def GetPopular(Startpage: int = 1, Endpage: int = 20)-> dict[str, str]:
    '''
    Returns dictionnary of actors in the "most popular" tab,
    from page 1 to EndPage by default.
    The dictionnary includes their 'names' as keys, and original langage of their most popular movie as 'values'
    Does not add any actor to the return dictionary that doesn't have a 'en' (english as primary spoken language) movie as their most popular movie.
    (Because the most popular list is filled with unknown actors that are extremely niche to certain counrties)
    Does not add any actor that has any popular score in movies in their "known for" below 10 (or any values set in the "JeuCompletFilm" function)
    '''
    
    DictReturn ={}
    while Startpage < Endpage:
        url = f"https://api.themoviedb.org/3/person/popular?language=en&page={Startpage}"
        
        finito = requests.get(url, headers=headers)
        finito2 = json.loads(finito.text)
        
        number = 0
        try: #Try method necessary for list index out of range, in case movie doesn not have an original language set (happens often)
            for x in finito2['results']:
                print (x)
                if finito2['results'][number]['known_for'][0]['original_language'] != 'en':
                    #print(f"{finito2['results'][number]['name']} is not english but {finito2['results'][number]['known_for'][0]['original_language']}")
                    number +=1
                elif finito2['results'][number]['known_for'][0]['popularity'] < 10 and finito2['results'][number]['known_for'][1]['popularity'] < 10 and finito2['results'][number]['known_for'][2]['popularity'] < 10:
                    #print(f"{finito2['results'][number]['known_for'][0]['title']} has a popularity of {finito2['results'][number]['known_for'][0]['popularity']}, and every subsequent movie in the 'known for' category is below 10 too")
                    number +=1
                else:
                    DictReturn[finito2['results'][number]['name']] = finito2['results'][number]['known_for'][0]['original_language']
                    number +=1
            Startpage +=1
        except IndexError:
            Startpage +=1
            pass
    return DictReturn




ListPopularPeople = list(GetPopular().keys()) #1
def JeuCompletFilm() -> dict[str, str]:
    
    
    
    Debugging = random.choice(ListPopularPeople) #Chooses random person in the popular people list of the website
    DictFinal = {}
    DictFinal = DictMoviesOfActorID(FindPersonID(NameQueryInputActorDictPopularitySorted(str(Debugging))))
    
    Dico2 = {k:DictFinal[k] for k in DictFinal if DictFinal[k] > 12} #Minimum popularity of each movie to be in the list, BEFORE the check of "len(dico2) < 20" is doen
    
    
    if len(Dico2) < 15: #Number of movies the actor needs to be in to be in the list
        print ("Actor found not popular enough, search again")
        DictFinal.clear()
        Dico2.clear()
        return JeuCompletFilm()
        
    else:
        return Dico2

def ReduceDictToListOfTen(Dict: dict[str, str], SizeOfList:int = 5, NumberOfTopMovies:int = 3) -> list:
    '''Reduce Dictionnary to a List of (SizeOfList, 5 by default)
    appended by the top 3 movies of an actor by default (NumberOfTopMovies), by order ascending, no duplicates'''
    
    #print(f"message de reducedicttolistoften, Dict recu en argument : {Dict}") #debugging
    ListDictComplet = list(Dict)
    ListDictMinusThree = [] #Three in variable name by default, but any size put in NumberOfTopMovies
    for x in ListDictComplet:
        ListDictMinusThree.append(x)
    for j in range(NumberOfTopMovies):
        ListDictMinusThree.pop()
    
    number = 1
    FilmReturn = []
    for x in range(SizeOfList):
        FilmReturn.append(ListDictMinusThree[round(len(ListDictMinusThree) / (SizeOfList/number))-1]) #Makes a list of 10 movies, located at the 1/10th, 2/10th, 3/10th etc... length of the movie list, the "5th" being the "SizeOfList" variable
        number +=1
    FinalListAppend = ListDictComplet[:-abs(NumberOfTopMovies)-1:-1]
    FinalListAppend.reverse()
    for x in FinalListAppend:
        FilmReturn.append(x) #Appends the top 3 (or any number in NumberOfTopMovies) movies of the actor to the list of movies
    
    
    return FilmReturn

def Working_Game(loop: int = 0):
    '''
    Makes the game works in terminal, 
    not used in the Tkinter version of the game
    '''
    Dico2 = {}
    Dico2 = JeuCompletFilm()
    
    DicoListe = ReduceDictToListOfTen(Dico2)
    
    for key in DicoListe:    
        print(f'{key}, released in : {GetReleaseYearOfMovie(key)}')
        
        PlayerGuess = pyip.inputStr("Enter name of the actor that played in all of those movies : >")
        recherche = tmdb.Search().person(query=f'{PlayerGuess}')
        try:
            if recherche['results'][0]['name'] == NameToGuess:
                print(f'Bien joue la team') #User found the correct name
                sys.exit()
            
            else:
                print(f"Non, ce n'est pas {recherche['results'][0]['name']}")
        except IndexError:
            print('No results for this name, try again')
            loop +=1
            continue

        if loop == len(DicoListe)-4: #Prints when the user has reached 3 last movies, they are the top 3 movies in popularity of the actor
            print ("3 most popular movies :")        
        
        if (loop) == len(DicoListe)-1:
            print("fin du jeu")
            
            sys.exit()
        loop +=1




#response = tmdb.People(95101).info() #Gets the info from the FindActorID function
#print (response)
def GetActorInfoOnID():
    response = tmdb.People(95101).info() #Gets the info from the FindActorID function
    poster = response['profile_path']
    ActorFace = f"https://image.tmdb.org/t/p/original{poster}"
    Actorbiography = response['biography']
    





NumberOfGuess = 0
Liste3 = ReduceDictToListOfTen(JeuCompletFilm()) #2
def GetListItem(): 
    global NumberOfGuess
    try: 
        MovieToGuess = (f"{Liste3[NumberOfGuess]} ({GetReleaseYearOfMovie(Liste3[NumberOfGuess])})")        
        NumberOfGuess+=1
    except IndexError:
        ###########################
        NumberOfGuess+=1
    return MovieToGuess

def GetGenreItem(): 
    global NumberOfGuess
    try: 
        GenreGlobal = (f"Genre : {GetGenreOfMovie(Liste3[NumberOfGuess-1])}")
    except IndexError:
        pass
    return GenreGlobal
    


def GetPopularityOfMovie(MovieName: str) -> str:
    annee = ""
    search = tmdb.Search()
    response = search.movie(query=f"{MovieName}")
    for j in search.results:
        annee = str((j['popularity']))
        if len(annee) == 0:
            return "No data on release date"
        break
    return annee #was cloned from the "get year of movie" function

def GetGenreOfMovie(MovieName: str) -> str:
    genre = ""
    search = tmdb.Search()
    response = search.movie(query=f"{MovieName}")
    testos = response['results'][0]['genre_ids']
    listgenre = []
    for x in testos:
        listgenre.append(genreAPI[x])
    
    listgenre2 = ", ".join(listgenre)
    return listgenre2

genreAPI = {28: 'Action',
            12: 'Adventure',
            16: 'Animation',
            35: 'Comedy',
            80: 'Crime',
            99: 'Documentary',
            18: 'Drama',
            10751: 'Family',
            14: 'Fantasy',
            36: 'History',
            27: 'Horror',
            10749: 'Romance',
            9648: 'Mystery',
            10402: 'Music',
            878: 'Science Fiction',
            10770: 'TV Movie',
            53: 'Thriller',
            10752: 'War',
            37: 'Western'}
        


def GetPictureOne(IDActor):
    
    images = tmdb.People(IDActor).images()
    for image in images['profiles'][0]['file_path']:
        return images['profiles'][0]['file_path']
    
