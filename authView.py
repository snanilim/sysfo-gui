import tkinter as tk
from tkinter import font
import requests
import json
import pprint

root = tk.Tk()

def get_info(userid, password):
    print(f'user ID {userid}, password {password}')


WIDTH = 600
HEIGHT = 400
FrameBack = '#c1c1c1'
# 9eabaa

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="img/back-04.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg=FrameBack, bd=5)
frame.place(relx=0.5, rely=0.10, relwidth=0.80, relheight=0.80, anchor='n')

label = tk.Label(frame, bg=FrameBack, font=('Courier', 22), text="Login", justify='left')
label.place(relwidth=1, relheight=0.2)

userIDLabel = tk.Label(frame, bg=FrameBack, font=('Courier', 15), text="UserID:", justify='left')
userIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')

userIDEntry = tk.Entry(frame, font=('Courier', 15))
userIDEntry.place(relx=0.30, rely=0.25, relwidth=0.6, relheight=0.12)


passwordLabel = tk.Label(frame, bg=FrameBack, font=('Courier', 15), text="Password:", justify='left')
passwordLabel.place(relx=0.03, rely=0.45, relwidth=0.3, relheight=0.12, anchor='nw')

passwordEntry = tk.Entry(frame, font=('Courier', 15), show="*",)
passwordEntry.place(relx=0.30, rely=0.45, relwidth=0.6, relheight=0.12)

button = tk.Button(frame, text="Submit", font=('Courier', 12), bg="#749492", command=lambda: get_info(userIDEntry.get(), passwordEntry.get()))
button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)




root.mainloop()

# 749492

