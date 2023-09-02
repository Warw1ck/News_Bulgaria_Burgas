from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.configure(background='black')
    root.title('Burgas news')
    root.resizable(False, False)
    root.geometry("400x600")

    return root


def create_frame():
    frame = Canvas(root, width=400, height=600)
    frame.grid(row=0, column=0)
    frame.configure(bg='#19647E')
    return frame


root = create_root()
frame = create_frame()
