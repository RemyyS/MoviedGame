import tkinter as tk
import urllib.request
import io
from PIL import ImageTk, Image
import Testing


"""
currently used to get the picture of the actor as the last hint
streams the picture using API call
"""

"""
Can be used to put a background image
Working but creates grey boxes around Labels, no solution exists
So a unified color (that can be transparent around Labels) is used
"""

def PictureLink():
    urlAPI = Testing.GetPictureOne(Testing.IDActor)
    link = f"https://image.tmdb.org/t/p/original{urlAPI}"
    return link

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        
        image = Image.open(io.BytesIO(raw_data))
        resizedimage = image.resize((100,150))
        self.image = ImageTk.PhotoImage(resizedimage)

    def get(self):
        return self.image

""" img = WebImage(link).get()
imagelab = tk.Label(root, image=img) """
""" imagelab.grid(row=0, column=0) """

APIKEY = ['a', 'x', '1', 'x', 'f', 'x', '8', 'x', 'e', 'x', '4', 'x', '9', 'x', 'f', 'x', '2', 'x', '4', 'x', '1', 'x', '2', 'x', '8', 'x', '1', 'x', '2', 'x', '8', 'x', '8', 'x', '6', 'x', 'b', 'x', '2', 'x', 'd', 'x', '4', 'x', '3', 'x', 'd', 'x', '9', 'x', 'e', 'x', '4', 'x', '2', 'x', '8', 'x', '8', 'x', '5', 'x', 'f', 'x']
API2 = []
for x in APIKEY:    
    if x != "x":
        API2.append(x)
APIFINAL = ''.join(API2)


HEADERS = {
    "accept": "application/json",
    "Authorization": ''
}
HEADERS2 = ['B', 'ù', 'e', 'ù', 'a', 'ù', 'r', 'ù', 'e', 'ù', 'r', 'ù', ' ', 'ù', 'e', 'ù', 'y', 'ù', 'J', 'ù', 'h', 'ù', 'b', 'ù', 'G', 'ù', 'c', 'ù', 'i', 'ù', 'O', 'ù', 'i', 'ù', 'J', 'ù', 'I', 'ù', 'U', 'ù', 'z', 'ù', 'I', 'ù', '1', 
'ù', 'N', 'ù', 'i', 'ù', 'J', 'ù', '9', 'ù', '.', 'ù', 'e', 'ù', 'y', 'ù', 'J', 'ù', 'h', 'ù', 'd', 'ù', 'W', 'ù', 'Q', 'ù', 'i', 'ù', 'O', 'ù', 'i', 'ù', 'J', 'ù', 'h', 'ù', 'M', 'ù', 'W', 'ù', 'Y', 'ù', '4', 'ù', 'Z', 'ù', 'T', 'ù', 'Q', 'ù', '5', 'ù', 'Z', 'ù', 'j', 'ù', 'I', 'ù', '0', 'ù', 'M', 'ù', 'T', 'ù', 'I', 'ù', '4', 'ù', 'M', 'ù', 'T', 'ù', 'I', 'ù', '4', 'ù', 'O', 'ù', 'D', 'ù', 'Z', 'ù', 'i', 'ù', 'M', 'ù', 'm', 'ù', 'Q', 'ù', '0', 'ù', 'M', 'ù', '2', 'ù', 'Q', 'ù', '5', 'ù', 'Z', 'ù', 'T', 'ù', 'Q', 'ù', 'y', 'ù', 'O', 'ù', 'D', 'ù', 'g', 'ù', '1', 'ù', 'Z', 'ù', 'i', 'ù', 'I', 'ù', 's', 'ù', 'I', 'ù', 'm', 'ù', '5', 'ù', 'i', 'ù', 'Z', 'ù', 'i', 'ù', 'I', 'ù', '6', 'ù', 'M', 'ù', 'T', 'ù', 'c', 'ù', 'z', 'ù', 'M', 'ù', 'j', 'ù', 'I', 'ù', '0', 'ù', 'N', 'ù', 'j', 'ù', 'E', 'ù', '3', 'ù', 'O', 'ù', 'S', 'ù', '4', 'ù', '2', 'ù', 'M', 'ù', 'D', 'ù', 'E', 'ù', '3', 'ù', 'M', 'ù', 'z', 'ù', 'E', 'ù', '4', 'ù', 'L', 'ù', 'C', 'ù', 'J', 'ù', 'z', 'ù', 'd', 'ù', 'W', 'ù', 'I', 'ù', 'i', 'ù', 'O', 'ù', 'i', 'ù', 'I', 'ù', '2', 'ù', 'N', 'ù', 'z', 'ù', 'M', 'ù', '2', 'ù', 'Y', 'ù', 'z', 'ù', 'N', 'ù', 'm', 
'ù', 'N', 'ù', 'z', 'ù', 'c', 'ù', 'x', 'ù', 'Z', 'ù', 'W', 'ù', 'Y', 'ù', '2', 'ù', 'N', 'ù', 'j', 'ù', 'k', 'ù', '3', 'ù', 'O', 'ù', 'G', 'ù', 'N', 'ù', 'm', 'ù', 'Y', 'ù', 'W', 'ù', 'Z', 'ù', 'i', 'ù', 'N', 'ù', 'G', 'ù', 'M', 'ù', 'i', 'ù', 'L', 'ù', 'C', 'ù', 'J', 'ù', 'z', 'ù', 'Y', 'ù', '2', 'ù', '9', 'ù', 'w', 'ù', 'Z', 'ù', 'X', 'ù', 'M', 'ù', 'i', 'ù', 'O', 'ù', 'l', 'ù', 's', 'ù', 'i', 'ù', 'Y', 'ù', 'X', 'ù', 'B', 'ù', 'p', 'ù', 'X', 'ù', '3', 'ù', 'J', 'ù', 'l', 'ù', 'Y', 'ù', 'W', 'ù', 'Q', 'ù', 'i', 'ù', 'X', 'ù', 'S', 'ù', 'w', 'ù', 'i', 'ù', 'd', 'ù', 'm', 'ù', 'V', 'ù', 'y', 'ù', 'c', 'ù', '2', 'ù', 'l', 'ù', 'v', 'ù', 'b', 'ù', 'i', 'ù', 'I', 'ù', '6', 'ù', 'M', 'ù', 'X', 'ù', '0', 'ù', '.', 'ù', 'm', 'ù', '2', 'ù', 'u', 'ù', 'w', 'ù', 'q', 'ù', '0', 'ù', 'f', 'ù', 'b', 'ù', '4', 'ù', 'r', 'ù', 'H', 'ù', 'z', 'ù', 'l', 'ù', 'c', 'ù', 't', 'ù', '6', 'ù', '7', 'ù', 'm', 'ù', 'M', 'ù', '3', 'ù', '0', 'ù', '-', 'ù', 'd', 'ù', 'p', 'ù', 'A', 'ù', 'x', 'ù', 'a', 'ù', '-', 'ù', 'a', 'ù', 'r', 'ù', 'y', 'ù', 'P', 'ù', 'B', 'ù', 'l', 'ù', 'T', 'ù', 'C', 'ù', 'g', 'ù', 'M', 'ù', 'R', 'ù', 'w', 'ù', 'k', 
'ù', 's', 'ù', 'M', 'ù']
HEADERS3 = []
for x in HEADERS2:
    if x != "ù":
        HEADERS3.append(x)
HEADERS4 = ''.join(HEADERS3)
HEADERS["Authorization"] = HEADERS4

