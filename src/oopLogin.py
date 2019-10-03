import tkinter as tk
from tkinter import font
import requests
import json
import pprint

import re, uuid
import time
from tkinter import scrolledtext
import datetime
import os
from client_mqtt import MQTTClient

from get_data import *

class GetData(object):
    def registrationInfo(self):
        data = {
            "info": 1,
            "status": 1,
            "idle": 0,
            "cpu": 1,
            "memory": 1,
            "disk": 1,
            "process": 0,
            "network": 0
        }
        res_info = getData(data)
        return res_info

        

# client = MQTTClient()


class Container(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.title("Python GUI")
        # win = tk.Tk()               # Create instance 
        self.winfo_toplevel().title("Sheikh Rasel Digital Lab")

        WIDTH = 600
        HEIGHT = 400
        FrameBack = '#a19eae'

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.background_image = tk.PhotoImage(file="./img/login-background-8.png")
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
        # self.show_frame(InfoPage)

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

        button = tk.Button(self, text="Submit", font=('Courier', 12), bg="#555c9c", command=lambda: get_info(userIDEntry.get(), passwordEntry.get(), controller))
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

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        canvas = tk.Canvas(self)
        canvas.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)

        frame = tk.Frame(canvas)
        # resize the canvas scrollregion each time the size of the frame changes
        frame.bind('<Configure>', on_configure)
        # display frame inside the canvas
        canvas.create_window(1, 0, window=frame)

        scrolly = tk.Scrollbar(self, command=canvas.yview)
        scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
        canvas.configure(yscrollcommand=scrolly.set)


        get_data = GetData()
        data = get_data.registrationInfo()

        res_info = json.dumps(data)

        cpu_info = data['cpu_info']
        memory_info = data['memory_info']
        disk_info = data['disk_info']

        def bytesTo(bytes, to, bazeSize=1024):
            rangeNum = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
            total = bytes
            for i in range(rangeNum[to]):
                total = total / bazeSize
            return round(total,3)

        # print(bytesTo(8277684224, 'g'))

        # print('data', data)

        label = tk.Label(self, font=('Courier', 18), text="Device Registration Info", justify='left')
        label.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        cpu = tk.Label(frame, font=('Courier', 14), text=f"CPU Information:", justify='left', anchor='w')
        cpu.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        tk.Label(frame, font=('Courier', 10), text=f"Brand: {cpu_info['brand']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Manufacturer: {cpu_info['vendor_id']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Version: {cpu_info['cpuinfo_version']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Bits: {cpu_info['bits']} bits", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        space = tk.Label(frame, font=('Courier', 14), text="", justify='left', anchor='w')
        space.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        ram = tk.Label(frame, font=('Courier', 14), text="Ram Information:", justify='left', anchor='w')
        ram.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        tk.Label(frame, font=('Courier', 10), text=f"Total: {bytesTo(memory_info['total'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Used: {bytesTo(memory_info['used'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Free: {bytesTo(memory_info['total'] - memory_info['used'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"percent: {memory_info['percent']}%", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        space = tk.Label(frame, font=('Courier', 14), text="", justify='left', anchor='w')
        space.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        disk = tk.Label(frame, font=('Courier', 14), text="Disk Information:", justify='left', anchor='w')
        disk.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        tk.Label(frame, font=('Courier', 10), text=f"Total: {bytesTo(disk_info['total'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Used: {bytesTo(disk_info['used'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        tk.Label(frame, font=('Courier', 10), text=f"Free: {bytesTo(disk_info['free'], 'g')} Gib", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        space = tk.Label(frame, font=('Courier', 14), text="", justify='left', anchor='w')
        space.pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)

        button = tk.Button(frame, text="Submit", font=('Courier', 12), bg="#749492", command=lambda: get_info(res_info, controller))
        button.pack(side = tk.RIGHT, fill=tk.BOTH, expand=tk.FALSE)

        def get_info(info, controller):
            print(f'lab ID {info}')

            # mqtt start
            client = MQTTClient()
            info = {"info" : info}
            client.on_publish('srdl/reginfo/', info)
            client.on_loop_forever()
            result = client.result
            # mqtt end

            if result:
                print('result', result)
                device_uuid = '09101u32cnwc0'
                auth_token = f'this is auth token of device id {device_uuid}'
                today = datetime.datetime.now()
                token_obj = {
                    "device_uuid": device_uuid,
                    "auth_token": auth_token,
                    "date": today
                }
                dirPath = os.path.dirname(os.path.abspath(__file__))
                fileWrite = open(f"{dirPath}/config/conf-01.txt", "w")
                def enc(str):
	                return ' '.join(bin(ord(char)).split('b')[1].rjust(8, '0') for char in str)
                token_obj = enc(str(token_obj))
                fileWrite.write(token_obj)
                fileWrite.close()

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

