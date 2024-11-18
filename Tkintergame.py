from tkinter import * 
import tmdbsimple as tmdb
import requests
import json
import pprint
import random
import Testing

tmdb.API_KEY = '5046bd40ead6143ad0243a87775b1ff1'
tmdb.REQUESTS_TIMEOUT = (5, 10)
tmdb.REQUESTS_SESSION = requests.Session()

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MDQ2YmQ0MGVhZDYxNDNhZDAyNDNhODc3NzViMWZmMSIsIm5iZiI6MTczMTY0MzgwOS43MDIyNTA3LCJzdWIiOiI2NzM2YzNmNzcxZWY2Njk3OGNmYWZiNGMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.XjqyInYwlKE8VzRX_SWART2QtHU09gDfgzx7jfaPkKs"
}

print (Testing.OrganiserLeDico(Testing.Returns_Dictionary_Of_Movies_Sorted_By_Popularity_Of_An_Actor_ID(Testing.Finding_Person_ID(Testing.Input_Name_Query_Returns_Actor_Dictionary_Sorted_By_Popularity("Watson")))))











