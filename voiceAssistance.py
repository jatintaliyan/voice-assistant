import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

gali = ["ki maa ka bhosda","lund le le", "lodu","gandu","chakka","lund se muu ka","aandal","ki dhhii ki chut","chutia"]



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("how can i help you")

def takeCommand():
    #it takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'say something' in query:
            speak(' -----     aaah gaand dee gha keee ithnee gooor seee suunn raah')
        
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,2)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'open firefox' in query:
            firefoxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefoxPath)

        elif 'mayank' in query:
            print('lund le le gandu')
            speak(f"mayank {gali[random.randint(0,9)]}")

        elif 'manu' in query:
            print('lund le le gandu')
            speak(f"manu {gali[random.randint(0,9)]}")
        elif 'vansh' in query:
            print('lund le le gandu')
            speak(f"vansh {gali[random.randint(0,9)]}")

        elif 'krish' in query:
            print('lund le le gandu')
            speak(f"krish {gali[random.randint(0,9)]}")

        elif 'rajat' in query:
            print('lund le le gandu')
            speak(f"rajat {gali[random.randint(0,9)]}")

        elif 'bhosdi ke' in query:
            print('aukat me')
            speak("lodu gaalii kiisse dee raah")

           
              
    

        elif 'close' in query:
            speak("good day sir")
            break

