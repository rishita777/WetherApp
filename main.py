import win32com.client as wincom
import requests
import json

city=input("Enter name of city :")
speak = wincom.Dispatch("SAPI.SpVoice")
url=f"https://api.weatherapi.com/v1/current.json?key=3bd28aaa8317452388c141634231107&q={city}"
r=requests.get(url)
print(r.text)

dic1=json.loads(r.text)
w=dic1["current"]["temp_c"]
w1=dic1["location"]["region"]
w2=dic1["location"]["country"]
h=dic1["current"]["humidity"]
p=dic1["current"]["precip_mm"]
speak.Speak(f"{city} located in state {w1} country {w2}'s current wether in {w} degrees."
            f"The humidity is {h} , precipitation {p} ")


