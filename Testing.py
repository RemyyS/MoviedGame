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
def FindingPersonID(NameOfPerson: str) -> str:
    recherche = tmdb.Search()
    reponse = recherche.person(query=f"{NameOfPerson}")
    for j in recherche.results:
        return j['id']
    
rangemovienumber = 100
movienumber = 0
response = tmdb.People(103).movie_credits()

try:
    for t in range(rangemovienumber):
        print (response['cast'][movienumber]['title'], ":", response['cast'][movienumber]['popularity'])
        print("")
        movienumber +=1
except IndexError:
    pass




        