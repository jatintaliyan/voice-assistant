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

def words_to_numbers(text):
    word_to_digit = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000
    }

    words = text.split()
    number = 0
    current = 0

    for word in words:
        if word in word_to_digit:
            current += word_to_digit[word]
        elif word == "hundred" and current != 0:
            current *= 100
        elif word == "thousand" and current != 0:
            number += current * 1000
            current = 0

    return number + current

# # Example:
# text = "twenty-one"
# print(f"Converted to number: {words_to_numbers(text)}")  # Output: 21


def search_on_youtube(query):
    # Replace spaces with '+' for a proper URL
    query = query.replace(' ', '+')
    # Construct the YouTube search URL
    search_url = f"https://www.youtube.com/results?search_query={query}"
    # Open the search URL in the default web browser (or specify Firefox if needed)
    webbrowser.open(search_url)

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

def takeNumber():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        text = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {text}\n")
        number = int(text)

    except Exception as e:
        print("say that again please...")
        return 'None'
    
    return number

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
        
        elif 'search youtube' in query:
            speak("what do you want to search")
            search_term = takeCommand()
            search_on_youtube(search_term)
        
        elif 'addition' in query:
            speak("proceeding addition")
            speak('tell me the first number')
            num1 = takeNumber()
            speak('tell me the second number')
            num2 = takeNumber()
            speak(f"the sum is {num1+num2}")

        elif 'close' in query:
            speak("good day sir")
            break