import webbrowser
from canvas1 import frame


def clean():
    frame.delete("screen")


def open_link(link):
    webbrowser.open(link)
