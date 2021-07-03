import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import winshell
import os
import requests
from bs4 import BeautifulSoup
import webbrowser as wb
import pywhatkit

engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speak() uses sapi5 voice to answer

def speak(text):
    engine.say(text)
    engine.runAndWait()

#wish() wishes Good Morning/Afternoon/Evening using date time module

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning Sohail!")

    elif hour>=12 and hour<=15:
        speak("Good Afternoon Sohail!")

    elif hour>15 and hour<=19:
        speak("Good Evening Sohail!")

    speak(" Hey this is your voice assistant Tim , how may I help you ?")

#takecommand() will listen my command using speechRecognition module

def takecommand():

    r = sr.Recognizer()
    print("Listening... ")
    r.pause_threshhold = 0.8
    with sr.Microphone() as source:
        audio=r.listen(source)

        try:
            print('Recognizing...')
            command=r.recognize_google(audio,language="en-IN")
            print(f" {command}")

        except Exception as e:
            print("Say that Again ")

    return command

def note(text):
    date=datetime.datetime.now
    pass

def weather():
    search = takecommand()
    url = f"https://www.google.com/search?q= {search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    print(temp)


def emptybin():

    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

    except Exception as e:
        print("No items in Recycle bin")

    return "DELETED"

if __name__=="__main__":
    wish()
    query=takecommand().lower()

    while(True):

        if 'wikipedia' in query.lower():
            speak("Searching Wikipedia..")
            results = wikipedia.summary(query, sentences=1)
            speak(" According to Wikipedia ")
            print(results)
            speak(results)
            break

        elif 'open youtube' in query:
            url = 'youtube.com'
            chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            wb.register("chrome", None, wb.BackgroundBrowser(chromepath))
            wb.get('chrome').open_new_tab(url)
            break

        elif 'open google' in query:
            url='google.com'
            chromepath=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            wb.register("chrome",None,wb.BackgroundBrowser(chromepath))
            wb.get('chrome').open_new_tab(url)
            break

        elif 'open gmail' in query:
            url = 'gmail.com'
            chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            wb.register("chrome", None, wb.BackgroundBrowser(chromepath))
            wb.get('chrome').open_new_tab(url)
            break


        elif 'the time' in query:
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            speak(f"The time is {current_time}")
            break

        elif 'shutdown pc' in query:
            shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
            if shutdown == 'no':
                exit()
            else:
                os.system("shutdown /s /t 1")

            break

        elif 'open vscode' in query:
            vscodepath =r"C:\Users\Sohail\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(vscodepath)

        elif 'search ' in query:
            try:
                pywhatkit.search(query)
                print("Searching...")
                break

            except Exception as e:
                print("An unknown error occured")


        elif 'empty recycle bin' or 'delete all files from recycle bin ' in query:

            speak("Permanently  Deleting  all  files from  bin")
            emptybin()
            speak(" DELETED ")
            break

        elif 'what is your name robot' or 'who are you' in query :
            speak("My name is Tim and I am Sohail's virtual assistant")
            break









