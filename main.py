from tkinter import*
import requests
import time


def get_info(window):
    try:
        city = entry.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=34fe37d60a80fa46dff4d203f4496d6a"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp']-273.15)
        max_temp = int(json_data['main']['temp_max']-273.15)
        min_temp = int(json_data['main']['temp_min']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']-39600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']-39600))
        final_info = condition + "\n" + str(temp) + "°C"
        final_data = '\n' + "Max temp:" + str(max_temp) + "°C" + "\n" + "Min temp:"\
                     + str(min_temp) + "°C" +\
                     '\n' + "Pressure:" + str(pressure) +\
                     '\n' + "Humidity:" + str(humidity) + "kPa" + "\n"\
                     + "Wind speed:" + str(wind) +"km/h"
        label1.config(text=final_info)
        label2.config(text=final_data)
    except(KeyError):
        label1.config(text="Can not find this city")


window = Tk()
window.geometry("600x400")
window.title("Weather Forecast")
#bg = PhotoImage(file="cloud.png")
bg_label = Label(window)
bg_label.place(x=0, y=0)
f = ("Arial", 30, "bold")
t = ("Arial", 25)
entry = Entry(window, justify="center", font=f)

entry.pack()
entry.focus()
entry.bind('<Return>', get_info)
label1 = Label(window, font=t)
label1.pack()
label2 = Label(window, font=f)
label2.pack()
window.mainloop()
