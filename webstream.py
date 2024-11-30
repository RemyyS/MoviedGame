import tkinter as tk
import urllib.request
import io
from PIL import ImageTk, Image
import Testing

"""
Can be used to put a background image
Working but creates grey boxes around Labels, no solution exists
So a unified color (that can be transparent around Labels) is used
"""

urlAPI = Testing.GetPictureOne(Testing.IDActor)
link = f"https://image.tmdb.org/t/p/original{urlAPI}"
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

