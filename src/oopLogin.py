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
import platform
from client_mqtt import MQTTClient
from get_data import *
from helper import save_enc_data, crt_shortcut_save

class GetData(object):
    def registrationInfo(self):
        data = {
            "info": 1,
            "status": 1,
            "idle": 0,
            "cpu": 1,
            "memory": 1,
            "disk": 1,
            "motherboard": 1,
            "devices": 1,
            "process": 0,
            "network": 0
        }
        res_info = getData(data)
        return res_info

        

# client = MQTTClient()


class Container(tk.Tk):
    def __init__(self, *args, **kwargs):
        try:
            tk.Tk.__init__(self, *args, **kwargs)
            # tk.title("Python GUI")
            # win = tk.Tk()               # Create instance 
            self.winfo_toplevel().title("Sheikh Rasel Digital Lab")
            # self.device_uuid = str
            self.dirPath = str
            self.device_uuid = '76f08fa6-93e0-4314-96ff-f772fd3ed5d1'
            WIDTH = 650
            HEIGHT = 450
            if platform.system() == 'Linux':
                WIDTH = 600
                HEIGHT = 400
            elif platform.system() == 'Windows':
                WIDTH = 650
                HEIGHT = 450
        
            FrameColor = '#a19eae'
            ButtonColor = '#555c9c'

            canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
            canvas.pack()

            self.background_image = tk.PhotoImage(file=f"{args[0]}/img/login-background-8.png")
            background_label = tk.Label(master=self, image=self.background_image)
            background_label.place(relwidth=1, relheight=1)

            container = tk.Frame(self, bg=FrameColor, bd=5)
            container.place(relx=0.5, rely=0.10, relwidth=0.80, relheight=0.80, anchor='n')

            self.frames = {}

            for F in (LoginPage, LabIDPage, InfoPage, ErrorPage, SuccessPage):
                print(F)
                frame = F(container, self, FrameColor, ButtonColor)
                self.frames[F] = frame

                frame.place(relwidth=1, relheight=1)

            # self.show_frame(LoginPage)
            self.show_frame(InfoPage)
        except Exception as error:
            print('error', error)

    def show_frame(self, cont):
        print('cont', cont)
        print('self.frames', self.frames)
        frame = self.frames[cont]
        frame.tkraise()



def qf(param):
    print(param)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller, FrameColor, ButtonColor):
        try:
            tk.Frame.__init__(self, parent, bg=FrameColor)

            self.shouldDelete = True

            label = tk.Label(self, bg=FrameColor, font=('Courier', 22), text="Login", justify='left')
            label.place(relwidth=1, relheight=0.2)

            userIDLabel = tk.Label(self, bg=FrameColor, font=('Courier', 15), text="UserID:", justify='left')
            userIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')

            userIDEntry = tk.Entry(self, font=('Courier', 15))
            placeholder_text = 'yourmail@gmail.com'
            userIDEntry.insert(0, placeholder_text)
            userIDEntry.bind("<Button-1>", lambda event: clear_entry(event, userIDEntry))
            userIDEntry.place(relx=0.30, rely=0.25, relwidth=0.6, relheight=0.12)


            passwordLabel = tk.Label(self, bg=FrameColor, font=('Courier', 15), text="Password:", justify='left')
            passwordLabel.place(relx=0.03, rely=0.45, relwidth=0.3, relheight=0.12, anchor='nw')

            passwordEntry = tk.Entry(self, font=('Courier', 15), show="*",)
            passwordEntry.place(relx=0.30, rely=0.45, relwidth=0.6, relheight=0.12)

            button = tk.Button(self, text="Submit", font=('Courier', 12), bg=ButtonColor, command=lambda: get_info(userIDEntry.get(), passwordEntry.get(), controller))
            button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)
        except Exception as error:
            print('error', error)
        
        def clear_entry(event, entry):
            if self.shouldDelete:
                entry.delete(0, 'end')
                self.shouldDelete = False

        def get_info(userid, password, controller):
            try:
                print(f'user ID {userid}, password {password}')

                # mqtt start
                client = MQTTClient(controller.dirPath)
                client.dirPath = controller.dirPath
                mac_info = mac_addr()
                info = {"mac_addr" : mac_info, "user_id" : userid, "password": password}
                client.on_subscribe(f'srdl/res_login/{mac_info}/')
                client.on_publish('srdl/req_login/', info)
                client.on_loop_forever()
                print('client.msg', client.msg)
                result = eval(client.msg['result'])
                device_uuid = client.msg['device_uuid']
                controller.device_uuid = device_uuid
                # mqtt end

                if result:
                    print('result', result)
                    controller.show_frame(LabIDPage)
                else:
                    controller.show_frame(ErrorPage)
            except Exception as error:
                print('error', error)
            

class LabIDPage(tk.Frame):
    def __init__(self, parent, controller, FrameColor, ButtonColor):
        try:
            tk.Frame.__init__(self, parent, bg=FrameColor)

            label = tk.Label(self, bg=FrameColor, font=('Courier', 22), text="Lab ID", justify='left')
            label.place(relwidth=1, relheight=0.2)

            labIDLabel = tk.Label(self, bg=FrameColor, font=('Courier', 15), text="LabID:", justify='left')
            labIDLabel.place(relx=0.03, rely=0.25, relwidth=0.3, relheight=0.12, anchor='nw')

            labIDEntry = tk.Entry(self, font=('Courier', 15))
            labIDEntry.place(relx=0.30, rely=0.25, relwidth=0.6, relheight=0.12)

            button = tk.Button(self, text="Submit", font=('Courier', 12), bg=ButtonColor, command=lambda: get_info(labIDEntry.get(), controller))
            button.place(relx=0.35, rely=0.70, relheight=0.15, relwidth=0.4)
        except Exception as error:
            print('error', error)

        def get_info(labid, controller):
            try:
                print(f'lab ID {labid}')
                # mqtt start
                client = MQTTClient(controller.dirPath)
                client.dirPath = controller.dirPath
                mac_info = mac_addr()
                device_uuid = controller.device_uuid
                info = {"mac_addr": mac_info, "device_uuid": device_uuid, "lab_id" : labid}
                client.on_subscribe(f'srdl/res_lab/{device_uuid}/')
                client.on_publish(f'srdl/req_lab/{device_uuid}/', info)
                client.on_loop_forever()
                result = eval(client.msg['result'])
                print('result', result)
                # mqtt end

                if result:
                    print('result', result)
                    controller.show_frame(InfoPage)
                else:
                    controller.show_frame(ErrorPage)
            except Exception as error:
                print('error', error)


class InfoPage(tk.Frame):
    def __init__(self, parent, controller, FrameColor, ButtonColor):
        try:
            tk.Frame.__init__(self, parent, bg=FrameColor)

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

            # res_info = json.dumps(data)
            res_info = data

            cpu_info = data['cpu_info']
            memory_info = data['memory_info']
            disk_info = data['disk_info']
        except Exception as error:
            print('error', error)

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

        if platform.system() == 'Linux':
            tk.Label(frame, font=('Courier', 10), text=f"Brand: {cpu_info['brand']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            tk.Label(frame, font=('Courier', 10), text=f"Manufacturer: {cpu_info['vendor_id']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            tk.Label(frame, font=('Courier', 10), text=f"Version: {cpu_info['cpuinfo_version']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            tk.Label(frame, font=('Courier', 10), text=f"Bits: {cpu_info['bits']} bits", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
        elif platform.system() == 'Windows':
            tk.Label(frame, font=('Courier', 10), text=f"Brand: {cpu_info['Name']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            tk.Label(frame, font=('Courier', 10), text=f"Manufacturer: {cpu_info['Manufacturer']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            # tk.Label(frame, font=('Courier', 10), text=f"Version: {cpu_info['cpuinfo_version']}", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)
            tk.Label(frame, font=('Courier', 10), text=f"Bits: {cpu_info['AddressWidth']} bits", justify='left', anchor='w').pack(side = tk.TOP, fill=tk.BOTH, expand=tk.FALSE)


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

        button = tk.Button(frame, text="Submit", font=('Courier', 12), bg=ButtonColor, command=lambda: get_info(res_info, controller))
        button.pack(side = tk.RIGHT, fill=tk.BOTH, expand=tk.FALSE)

        def get_info(info, controller):
            try:
                print(f'lab ID {info}')

                # mqtt start
                client = MQTTClient(controller.dirPath)
                client.dirPath = controller.dirPath
                # info = {"info" : info}
                device_uuid = controller.device_uuid
                
                client.on_subscribe(f'srdl/res_reg/{device_uuid}/')
                client.on_publish(f'srdl/req_reg/{device_uuid}/', info)
                client.on_loop_forever()
                result = eval(client.msg['result'])
                lab_id = client.msg['lab_id']
                time_frame = client.msg['time_frame']
                # mqtt end

                if result:
                    print('result', result)
                    auth_token = f'this is auth token of device id {device_uuid}'
                    today = datetime.datetime.now()
                    token_obj = {
                        "device_uuid": device_uuid,
                        "auth_token": auth_token,
                        "date": today,
                        "time_frame": time_frame,
                        "lab_id": lab_id
                    }
                    save_enc_data(token_obj, controller.dirPath)
                    crt_shortcut_save(controller.dirPath)

                    controller.show_frame(SuccessPage)
                    
                    
                else:
                    controller.show_frame(ErrorPage)
            except Exception as error:
                print('error', error)


class SuccessPage(tk.Frame):
    def __init__(self, parent, controller, FrameColor, ButtonColor):
        try:
            tk.Frame.__init__(self, parent, bg=FrameColor)
            label = tk.Label(self, font=('Courier', 22), text="Login Successfull", fg="green")
            label.pack(pady=10, padx=10)

            # button1 = tk.Button(self, text="Close", command=lambda: controller.show_frame(LoginPage))
            button1 = tk.Button(self, text="Close", font=('Courier', 22), bg=ButtonColor, command=lambda: submit())
            button1.pack()
        except Exception as error:
            print('error', error)

        def submit():
            controller.quit()
            print('quit')


class ErrorPage(tk.Frame):
    def __init__(self, parent, controller, FrameColor, ButtonColor):
        try:
            tk.Frame.__init__(self, parent, bg=FrameColor)
            label = tk.Label(self, text="Something went wrong. Please try again", fg="red")
            label.pack(pady=10, padx=10)

            button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(LoginPage))
            button1.pack()
        except Exception as error:
            print('error', error)


def run_ooplogin(dirPath):
    try:
        app = Container(dirPath)
        app.dirPath = dirPath
        app.mainloop()
        app.destroy()
        client = MQTTClient(dirPath)
        client.dirPath = dirPath
        client.on_loop_forever()
    except Exception as error:
        print('error', error)


if __name__ == "__main__":
    app = Container()
    app.mainloop()
    app.destroy()
    client = MQTTClient()
    client.on_loop_forever()

