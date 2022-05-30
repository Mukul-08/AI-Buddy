import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
import requests
from requests import get
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Moring Sir!")
        speak("I am Jarvis please tell me how can i help you")
    
    elif hour>=12 and hour < 18:
        speak("Good Afternon Sir!")
        speak("I am Jarvis please tell me how can i help you")
    
    else:
        speak("Good Evening Sir!")
        speak("I am Jarvis please tell me how can i help you")
     

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(dp, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mk735728424@gmail.com', 'mukul7357#')
    server.sendmail('mk73572842@gmail.com', to, content)
    server.close()

if __name__== "__main__" :
  wishMe()
  while True:
   query = takeCommand().lower()

   if 'wikipedia'in query:
       speak('Searching in Wikipedia....')
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences=2)
       speak("According to Wikipedia")
       print(results)
       speak(results)
       
   elif 'open youtube' in query:
       webbrowser.open("youtube.com")
    
   elif "How are you" in query:
      speak("i m absloutely fine sir what about you")

   elif 'open takshila' in query:
       webbrowser.open("takshilaa.netlify.app")
       speak("Takshila is opend sir")

   elif 'play music' in query:
       music_dir = 'D:\Songs'
       songs = os.listdir(music_dir)
       rd = random.choice(songs)
       print(f"{rd}\n")
       os.startfile(os.path.join(music_dir, rd))
  
   elif 'the time' in query:
       strTime = datetime.datetime.now().strftime("%H:%M:%S")    
       speak(f"Sir, the time is {strTime}")
   
   elif 'open Code' in query:
       codepath = "C:\\Users\\atul\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(codepath)

   elif 'email to mukul' in query:
       try:
           speak("what to say?")
           content = takeCommand()
           to = "mk73572842@gmail.com"
           sendEmail(to, content)
           speak("Email has been sent!")
       except Exception as e:
            print(e)
            speak("Sorry sir can't able to sent mail")

   elif"send message" in query:
           pywhatkit.sendwhatmsg("+917357284241","This is Testig protocol",1,30 )
   
   elif "ip address" in query:
       ip = get('https://api.ipify.org').text
       speak(f"your ip adress is {ip}")


   elif "google" in query:
       speak("sir, what should i search on google")
       k = takeCommand().lower()
       webbrowser.open(f"{k}")

   elif "class" in query:
      speak("Yes Offcourse sir plz tell me the time when i have to attend your class")
      c = takeCommand().lower()
      speak("ohk sir i m taking your class")
      webbrowser.open("https://lovelyprofessionaluniversity.codetantra.com/secure/tla/mi.jsp?s=m&m=b6d5631a-68fa-3400-9ead-62311cdaaf55")

   elif "thanks" in query:
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
      speak("Thanks for using me sir, have a good day")

    elif hour>=16 and hour > 20:
      speak("Thanks for using me sir, have a good Evenging Sir")


    elif hour>=20 and hour > 0:
      speak("Thanks for using me sir, have a good Night Sir")
      
      sys.exit()


   
   elif "bhajan" in query:
       music_dir = 'D:\Songs'
       songs = os.listdir(music_dir)
       print(songs[18])
       os.startfile(os.path.join(music_dir, songs[18]))


   elif 'open Code' in query:
       codepath = "C:\\Users\\atul\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(codepath)

   elif "notepad" in query:
       speak("Opening Notepad in few seconds Sir")
       p = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
       os.startfile(p)

       speak("Anything Else Sir..")
    #   print("Anything Else Sir")
    

