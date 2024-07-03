import thinker as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c9217b9a82d8f5d124e158627f"
    json_data = request.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info = condition + "\n" + str(temp) "°C"
    final_data = "\n" + "Maksimum sıcaklık: " + str(max_temp) + "Minimum sıcaklık: " + str(min_temp) + "\n" + "Basınç: " + str(pressure) + "\n" + "Nem: " + str(humidity) + "\n" + "Rüzgar hızı: " + str(wind) + "\n" + "Gündoğumu: " + sunrise + "\n" + "Günbatımı: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
canvas = tk.TK()
canvas.geometry("600x500")
canvas.title("Hava durumu")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield..pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)
label1 = tk.label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font =f)
label2.pack()

canvas.mainplop()