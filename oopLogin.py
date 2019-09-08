import tkinter as tk
from tkinter import font
import requests
import json
import pprint

import paho.mqtt.client as mqtt
import re, uuid
import time


uuid.uuid4 # generating randorm number in base64
r = str(uuid.uuid4())
client = mqtt.Client(r)
broker = "broker.hivemq.com"
port = 1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

def on_message(client, userdata, message):
    print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
    check_topic(str(message.payload.decode("utf-8")))



client.on_connect = on_connect  #attach the callback function to the client object 
client.on_message = on_message	#attach the callback function to the client object

def check_topic(msg):
    print('msg', msg)
    client.loop_stop()
    client.disconnect()

class Container(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        WIDTH = 600
        HEIGHT = 400
        FrameBack = '#c1c1c1'

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.background_image = tk.PhotoImage(file="./img/back-04.png")
        background_label = tk.Label(master=self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        container = tk.Frame(self, bg=FrameBack, bd=5)
        container.place(relx=0.5, rely=0.10, relwidth=0.80, relheight=0.80, anchor='n')

        self.frames = {}

        for F in (LoginPage, PageOne):
            print(F)
            frame = F(container, self, FrameBack)
            self.frames[F] = frame

            frame.place(relwidth=1, relheight=1)

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        print('cont', cont)
        print('self.frames', self.frames)
        frame = self.frames[cont]
        frame.tkraise()



def qf(param):
    print(param)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller, FrameBack):
        tk.Frame.__init__(self, parent, bg=FrameBack)

        client.connect(broker,port,60)
        # client.loop_start()
        

        client.subscribe("srdl/res_login/", 1)
        
        label = tk.Label(self, bg=FrameBack, font=('Courier', 22), text="Login", justify='left')
        label.place(relwidth=1, relheight=0.2)

        userIDLabel = tk.Label(self, bg=FrameBack, font=('Courier', 15), text="UserID:", justify='left')
        userIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')

        userIDEntry = tk.Entry(self, font=('Courier', 15))
        userIDEntry.place(relx=0.30, rely=0.25, relwidth=0.6, relheight=0.12)


        passwordLabel = tk.Label(self, bg=FrameBack, font=('Courier', 15), text="Password:", justify='left')
        passwordLabel.place(relx=0.03, rely=0.45, relwidth=0.3, relheight=0.12, anchor='nw')

        passwordEntry = tk.Entry(self, font=('Courier', 15), show="*",)
        passwordEntry.place(relx=0.30, rely=0.45, relwidth=0.6, relheight=0.12)

        button = tk.Button(self, text="Submit", font=('Courier', 12), bg="#749492", command=lambda: get_info(userIDEntry.get(), passwordEntry.get(), controller))
        button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)

        def get_info(userid, password, controller):
            print(f'user ID {userid}, password {password}')


            
            # mqtt start
            
            client.publish("srdl/login/", "Hello world!")
            client.loop_forever()
            
            

            # mqtt end

            controller.show_frame(PageOne)
            

class PageOne(tk.Frame):
    def __init__(self, parent, controller, FrameBack):
        tk.Frame.__init__(self, parent, bg=FrameBack)
        label = tk.Label(self, text="Inner Page")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(LoginPage))
        button1.pack()





app = Container()
# app.check_topic('aaa')
app.mainloop()

