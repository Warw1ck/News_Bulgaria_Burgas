import urllib.request
from tkinter import Label
from PIL import ImageTk, Image
from canvas1 import root, frame
import requests
import json
from io import BytesIO


def create_image(news_image):
    try:
        URL = news_image
        u = urllib.request.urlopen(URL)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im.resize((400, 200)))
        images.append(photo)
        frame.create_image(200, 100, image=photo, tag="screen")
    except:
        path = 'images/2748558.png'
        img = ImageTk.PhotoImage(Image.open(path))
        images.append(img)
        frame.create_image(200, 100, image=img, tag="screen")


def news():
    query = 'Бургас'
    country = "BG"
    URL = f"https://api.newscatcherapi.com/v2/search?q=\"{query}\"&lang=bg&countries={country}"
    payload = {}
    #Get your API from newscatcherapi.com
    headers = {
        'X-API-KEY': 'YOUR-API'
    }
    r = requests.get(URL, headers=headers, data=payload)
    return json.loads(r.text)


def create_text(title, text):
    label1 = Label(root, text=text, wraplength=400, font='bold', bg='#28AFB0', fg='#1F271B')
    label2 = Label(root, text=title, wraplength=400, font='bold', bg='#28AFB0', fg='#1F271B')
    frame.create_window(200, 240, window=label2, tag="screen")
    frame.create_window(200, 360, window=label1, tag="screen")

images = []
