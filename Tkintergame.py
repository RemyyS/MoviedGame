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






 #Tri par popularité pour ne pas avoir un homonyme





