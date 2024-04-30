import pyttsx3   # text to speech
import speech_recognition as sr  # speech to text
import webbrowser # for web search use thisk
import datetime
import requests
import os
import time

def sptext():    #--> it will take input and convert to text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # <-- will search for surrounding noise and remove it  
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not Understand.")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)  # --> 1 lagny sy femal voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    engine.say(x)
    engine.runAndWait()

def KelvintoCelcius(K):
    C = K-273.15
    return "{:.2f}".format(C)

city = 'Karachi'
key = '3ff4b1100fef4f3f06b00e78af27b533'
url = f"https://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}"   

response = requests.get(url).json()

temp = KelvintoCelcius(response["main"]["temp"]) 
sky = response["weather"][0]["description"]   

if __name__ == "__main__":
    
    if "hey alexa" in sptext().lower():
        while True:
            data1 = sptext().lower()  # Convert to lowercase for easier comparison
            if "your name" in data1:
                name = "My name is Alexa and I am Voice assistant."
                speechtx(name)
            
            elif "your crush" in data1:
                crush = "I don't have feelings for humans because I am python based model."
                speechtx(crush)
            
            elif "time right now" in data1:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speechtx(f"Current Local Time is {time}")
            
            elif "current month" in data1:
                month = datetime.datetime.now().strftime("%B")
                speechtx(f"Current month ongoing is {month}")
            
            elif "current day" in data1:
                day = datetime.datetime.now().strftime("%A")
                speechtx(f"Current day is {day}")
            
            elif "current year" in data1:
                year = datetime.datetime.now().strftime("%Y")
                speechtx(f"Current year is {year}")
            
            elif "your creator" in data1:
                creator = "I was made by Meesam Abbas, a well-known Python programmer."
                speechtx(creator)
            
            elif "open google" in data1:
                webbrowser.open("https://www.google.com/")
            
            elif "open youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            
            elif "weather" in data1:
                speechtx(sky)
            
            elif "temperature" in data1:
                speechtx(f"temprature now is {temp} centigrade.")    
            
            elif "play song" in data1:
                address = "Put your addreess over here where your songs are present"
                listsong = os.listdir(address)
                os.startfile(os.path.join(address,listsong[0]))
            
            elif "exit" in data1:
                bye = "Bye, Take care."
                speechtx(bye)
                break
            else: 
                speechtx("Sorry couldn't hear that")
                
            time.sleep(4)
