import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''its gives audio wish to the user'''
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour<12 :
        speak("Good Morning!")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you? ")    

def takeCommand():
    '''it takes micropohone input from user and returns string output'''
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language ='en-in')
        print('user said:',query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None" 
    return query       

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("pandeysamaira0@gmail.com","samaira@22")
    server.sendmail("pandeysamaira0@gmail.com",to,content)
    server.close()

if __name__ =="__main__":
    # speak("Hello Saumya, What's Up")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic to build tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')    
        elif 'open google' in query:
            webbrowser.open('google.com')    
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')    
        elif 'play music' in query:
            music_dir = ""   
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
        elif 'open code' in query:
            codepath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to saumya' in query:
            try:
                speak('What should I say')
                content = takeCommand()
                to = "saumyaswati2016@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend, can't send the mail")

        elif "weather" in query:
            search = "weather in Patna"  
            url = f"https://www.google.com/search?q={search}"  
            r = requests.get(url) 
            data = BeautifulSoup(r.text,"html.parser") 
            temp =data.find("div", class_="BNeawe").text 
            speak(f"current {search} is {temp}") 

        elif 'quit' in query:
            exit()

             


