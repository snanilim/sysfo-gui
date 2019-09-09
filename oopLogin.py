import tkinter as tk
from tkinter import font
import requests
import json
import pprint

import paho.mqtt.client as mqtt
import re, uuid
import time



class MQTTClient(object):
    def __init__(self, *args, **kwargs):
        try:
            uuid.uuid4
            r = str(uuid.uuid4())
            
            self.result = bool
            self.msg = dict

            self.BROKER_IP = "broker.hivemq.com"
            self.PORT = 1883

            self.client = mqtt.Client(r)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.BROKER_IP, self.PORT, 60)

            print(f"Connected to {0}, starting MQTT loop")
            # self.client.loop_forever()
            # self.client.loop_start()
        except Exception as e:
            print("error", e)

    def on_message(self,client,userdata,message):
        print("topic: "+message.topic+"	"+"payload: "+str(message.payload.decode("utf-8")))
        msg = str(message.payload.decode("utf-8"))
        data = json.loads(msg)
        value = data.get("result", "")
        self.result = eval(value)
        self.on_loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("srdl/res_login/", 1)

    def on_publish(self, topicUri, message):
        topic = message
        topic_dump = json.dumps(topic)
        self.client.publish(topicUri, topic_dump)
        print('Publish')

    def on_loop_forever(self):
        print('work')
        self.client.loop_forever()

    def on_loop_stop(self):
        print('work')
        self.client.loop_stop()
        self.client.disconnect()

        

# client = MQTTClient()
        


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

        for F in (LoginPage, LabIDPage, InfoPage, ErrorPage):
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
            client = MQTTClient()
            info = {"userid" : userid, "password": password}
            client.on_publish('srdl/login/', info)
            client.on_loop_forever()
            result = client.result
            # mqtt end

            if result:
                print('result', result)
                controller.show_frame(LabIDPage)
            else:
                controller.show_frame(ErrorPage)
            

class LabIDPage(tk.Frame):
    def __init__(self, parent, controller, FrameBack):
        tk.Frame.__init__(self, parent, bg=FrameBack)

        label = tk.Label(self, bg=FrameBack, font=('Courier', 22), text="Lab ID", justify='left')
        label.place(relwidth=1, relheight=0.2)

        labIDLabel = tk.Label(self, bg=FrameBack, font=('Courier', 15), text="LabID:", justify='left')
        labIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')

        labIDEntry = tk.Entry(self, font=('Courier', 15))
        labIDEntry.place(relx=0.30, rely=0.25, relwidth=0.6, relheight=0.12)


        button = tk.Button(self, text="Submit", font=('Courier', 12), bg="#749492", command=lambda: get_info(labIDEntry.get(), controller))
        button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)

        def get_info(labid, controller):
            print(f'lab ID {labid}')


            
            # mqtt start
            client = MQTTClient()
            info = {"labid" : labid}
            client.on_publish('srdl/labid/', info)
            client.on_loop_forever()
            result = client.result
            # mqtt end

            if result:
                print('result', result)
                controller.show_frame(InfoPage)
            else:
                controller.show_frame(ErrorPage)


class InfoPage(tk.Frame):
    def __init__(self, parent, controller, FrameBack):
        tk.Frame.__init__(self, parent, bg=FrameBack)

        label = tk.Label(self, bg=FrameBack, font=('Courier', 22), text="Info Page", justify='left')
        label.place(relwidth=1, relheight=0.2)

        labIDLabel = tk.Label(self, bg=FrameBack, font=('Courier', 15), text="CPU:", justify='left')
        labIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')



        button = tk.Button(self, text="Submit", font=('Courier', 12), bg="#749492", command=lambda: get_info("info", controller))
        button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)

        def get_info(info, controller):
            print(f'lab ID {info}')

            # mqtt start
            client = MQTTClient()
            info = {"info" : info}
            client.on_publish('srdl/labid/', info)
            client.on_loop_forever()
            result = client.result
            # mqtt end

            if result:
                print('result', result)
                # controller.show_frame(LabIDPage)
                app.quit()
                print('quit')
                
            else:
                controller.show_frame(ErrorPage)


class ErrorPage(tk.Frame):
    def __init__(self, parent, controller, FrameBack):
        tk.Frame.__init__(self, parent, bg=FrameBack)
        label = tk.Label(self, text="Something went wrong. Please try again", fg="red")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(LoginPage))
        button1.pack()





app = Container()
app.mainloop()
app.destroy()
client = MQTTClient()
client.on_loop_forever()

