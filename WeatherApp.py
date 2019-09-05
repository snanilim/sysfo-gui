import tkinter as tk
from tkinter import font
import requests
import json
import pprint

# 0025c7fb8bc4fd6a0e81ba396129d84b
def response_format(weather):
    try:
        name = weather['city']['name']
        country = weather['city']['country']
        
        lat = weather['city']['coord']['lat']
        lon = weather['city']['coord']['lon']

        date = weather['list'][1]['dt_txt']

        description = weather['list'][1]['weather'][0]['description']
        temp = weather['list'][1]['main']['temp']

        humidity = weather['list'][1]['main']['humidity']
        wind_speed = weather['list'][1]['wind']['speed']

        return_str = f' Country: {country} \n Name: {name} \n Lat: {lat} \n Lon: {lon} \n Date: {date} \n Description: {description} \n Temp (F): {temp} \n Humidity: {humidity} \n Wind speed: {wind_speed}'
    except:
        return_str = 'Some issue on \n this data or input data \n please provide correct city name'

    return return_str


def get_weather(city):
    weather_key = '0025c7fb8bc4fd6a0e81ba396129d84b'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = response_format(weather)

    # dumps = json.dumps(weather)
    # parsed = json.loads(dumps)
    # pprint.pprint(parsed)

    


HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="img/login-background-2.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 15), justify='left', bd=5)
label.place(relwidth=1, relheight=1)

root.mainloop()