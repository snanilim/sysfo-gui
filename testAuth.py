# import tkinter as tk
from tkinter import *
import requests
import json
import pprint


class MainView(Tk):
    # aaa = 11
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # container = Frame(self)
        root = Tk()

        WIDTH = 600
        HEIGHT = 400
        FrameBack = '#c1c1c1'
        # 9eabaa

        canvas = Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        background_image = PhotoImage(file="img/back-04.png")
        background_label = Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        




if __name__ == "__main__":
    root = MainView()
    # main = MainView(root)
    root.mainloop()