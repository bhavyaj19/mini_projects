from ast import main
import os
import time
import webbrowser
import speech_recognition as sr
from gtts import gTTS #txt-to-speech online
import pyttsx3 #text-to-speech offline
import playsound
import requests
# from AppOpener import run #Module uinstalled

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def google_search():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        inp=r.listen(source)
    try:
        print('Recognizing...')
        qry=r.recognize_google(inp)
        print('User said ',qry,'\n')
    except Exception as e:
        print('Exception: ',str(e))
        speak("I didn't understand")
        return "none"
    return qry

def weather(city):
    api_key ="ce85fe5f2d183c7249b473b6a76b99f0"
    base_url= "http://api.openweathermap.org/data/2.5/weather"
    request_url = f"{base_url}?appid={api_key}&q={city}"
    response = requests.get(request_url)

    if response.status_code==200:
        data = response.json()
        weather=data['weather'][0]['main']
        temp=round(data['main']['temp']-273.15, 2)  #round(some  int claculation,2) rounds it to 2 decimals
        print("Weather: ",weather.upper())
        print("Temperature: ",temp,"°C")

    else:
        print('error occured')
    return str(temp)

if __name__=='__main__':
    speak('Your wish is my command, master')
    while True:
        qry=google_search().lower()
        if 'youtube' in qry:
            speak('Opening YouTube')
            webbrowser.open('www.youtube.com')
            exit(0)            

        elif 'weather in' in qry:
            city=qry.split('weather in',1)[1]
            speak('Weather in '+city+'is: ')
            speak(weather(city)+'degree celcius')
            exit(0)

        elif 'dino' in qry:
            speak('opening chrome dino')
            webbrowser.open('https://chromedino.com/')
            exit(0)

        elif 'search' in qry:
            query=qry.split(' ',1)[1]
            webbrowser.open(query)
            exit(0)

        # elif 'epic game' in qry:
        #     try:    
        #         speak('opening epic games')
        #         run("epic games launcher")    #=========================Module uinstalled============================
        #     except:
        #         speak('Epic games not available ')
            exit(0)
