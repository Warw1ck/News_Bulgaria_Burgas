from tkinter import Button

from PIL import ImageTk, Image

from canvas1 import frame, root
from helper import open_link
import page


def left_button(n):
    path = 'images/left_arrow_1.png'
    img = ImageTk.PhotoImage(Image.open(path).resize((150, 80)))
    images.append(img)
    start_button_2 = Button(
        root,
        image=img,
        bg='#F4D35E',
        fg='#EE964B',
        borderwidth=0,
        command=lambda: page.page(n - 1)
    )
    frame.create_window(78, 560, window=start_button_2, tag="screen")


def right_button(n):
    path = 'images/right_arrow_1.png'
    img = ImageTk.PhotoImage(Image.open(path).resize((150, 80)))
    images.append(img)
    start_button_1 = Button(
        root,
        image=img,
        bg='#F4D35E',
        fg='#EE964B',
        borderwidth=0,
        command=lambda: page.page(n+1)
    )
    frame.create_window(324, 560, window=start_button_1, tag="screen")


def web_button(link):
    path = 'images/globle.png'
    img = ImageTk.PhotoImage(Image.open(path).resize((85, 85)))
    images.append(img)
    start_button_3 = Button(
        root,
        image=img,
        bg='#F4D35E',
        fg='#EE964B',
        borderwidth=0,
        command=lambda: open_link(link)
    )
    frame.create_window(200, 560, window=start_button_3, tag="screen")


images = []