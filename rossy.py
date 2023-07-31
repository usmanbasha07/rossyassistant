import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import subprocess
import smtplib
import pywhatkit
from googlesearch import search
import ast
import http.client


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon.")
    else :
        speak("Good Evening!")
    speak("Hello I am Rossy,your voice assistant,how can i help you.")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1 #wait gap for word to word while listening
        audio = r.listen(source)
    try:
        print("Recognizing..." )
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("I am not sure that you are talking to me.")
        print("Say that again please...")
        speak("I am not sure that you are talking to me,Say that again please.")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email', 'your_password')
    server.sendmail('your_email', to, content)
    server.close()



if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
       
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2) 
           speak("According to Wikipedia")
           print(results)
           speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Lenovo\\Music'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath ="C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'email to' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="peddintiusmanbasha@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Email  has not sended!")
        elif 'open whatsapp' in query:
            speak("opening Whatsapp")
            subprocess.Popen(["cmd", "/C", "start whatsapp://"], shell=True)
        elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            speak("playing "+query)
            pywhatkit.playonyt(query)
        elif 'search' in query:
            query = query.replace("search", "")
            speak("searching "+query+" on google")
            for j in search(query,num_results=10,lang="en"):
                print(j)
        elif 'stop' in query:
            print("Rossy:Okay Bye if you need help call me.\nSee you later.")
            speak("okay Bye, if you any need help call me")
            speak("See you later")
            break
        elif 'okay Bye' in query:
            print("Rossy:Okay Bye if you need help call me.\nSee you later.")
            speak("okay Bye, if you any need help call me")
            speak("See you later")
            break
        else:              
            conn = http.client.HTTPSConnection("random-stuff-api.p.rapidapi.com")

            headers = {
                'Authorization': "qtprB4WG8bYT",
                'X-RapidAPI-Key': "place_your_key",
                'X-RapidAPI-Host': "random-stuff-api.p.rapidapi.com"
                }
            query=query.replace(" ","%20")

            conn.request("GET", "/ai/response?message="+query+"&user_id=420", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data=data.decode("utf-8")
            mydata = ast.literal_eval(data)
            print("Rossy:"+repr(mydata["message"]))
            speak(repr(mydata["message"]))
            