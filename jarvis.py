import pyttsx3  # pip install pyttsx3 (For Speak)
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import psutil  # pip install psutil
import os  # (For system call)
import pyautogui  # pip install pyautogui (For Screenshot)
import pyjokes  # pip install pyjokes
import random
import json
from urllib.request import urlopen
import requests
import wolframalpha  # pip install wolframalpha (For Calculation)
import time
import operator

engine = pyttsx3.init()
app_id = 'api key'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  # for 24 hour clock
    speak("the current time is")
    speak(Time)
    # Time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12-hour clock
    # speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome Back Sir!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


def screenshot():
    img = pyautogui.screenshot()
    img.save("img path")


def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
          "I am created by you , "
          "I can help you in various regards , "
          "I can search for you on the Internet , "
          "I can also grab definitions for you from wikipedia , "
          "In layman terms , I can try to make your life a bed of roses , "
          "Where you just have to command me , and I will do it for you , ")


def Creator():
    speak("My creator is an extra-ordinary person ,"
          "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
          "He is very co-operative ,"
          "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")


if __name__ == '__main__':

    def clear():
        return os.system('cls')

    # This Function will clean any command before execution of this python file
    clear()

    wishme()

    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be stored here in 'query' and will be
        # converted to lower case for easily recognition of command

        if 'time' in query:
            time_()

        elif 'date' in query:
            date()

        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            speak("Searching...")
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+Search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'word' in query:
            speak("Opening MS Word......")
            word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(word)

        elif 'write a note' in query:
            speak("What should I write, Sir?")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should I include Date and Time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('Done Taking Notes, Sir!!')
            else:
                file.write(note)

        elif 'show notes' in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())
            print(file.read())

        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif 'play music' in query:
            video = 'video path'
            audio = 'audio path'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())

            if 'audio' in ans:
                songs_dir = audio
                songs = os.listdir(songs_dir)
                print(songs)
            elif 'video' in ans:
                songs_dir = video
                songs = os.listdir(songs_dir)
                print(songs)

            speak("select a random number")
            rand = (TakeCommand().lower())
            # used while loop to keep the jarvis on the speak command untill req. command is given.
            while('number' not in rand and rand != 'random' and rand != 'your choice'):
                # first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to requirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block.
                speak("I could not understand you. Please Try again.")
                rand = (TakeCommand().lower())

            if 'number' in rand:
                rand = int(rand.replace("number ", ""))
                os.startfile(os.path.join(songs_dir, songs[rand]))
                # 'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
                continue
            elif 'random' or 'your choice' in rand:
                rand = random.randint(1, 14)
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue

        elif 'news' in query:

            try:

                jsonObj = urlopen(
                    'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=30510bfc94f34b96bc9245177fb32446')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the techcrunch')
                print(' == == == == == == == = TOP HEADLINES == == == == == ==' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))

        # show location on map
        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # calculation
        elif 'calculate' in query:

            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        # General Questions
        elif "what is" in query or "who is" in query:

            # Use the same API key that we have generated earlier
            client = wolframalpha.Client(app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        # sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        # OS commands
        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        # quit
        elif 'offline' in query:
            speak("Going Offline Sir!!.....ThankYou!!")
            quit()

        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()

        elif 'tell me about your creator' and 'creator' in query:
            Creator()

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")

        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")

        elif "why you came to this world" in query:
            speak("Thanks to you. further it is a secret")

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
                  "And I think it is just a mere illusion , "
                  "It is waste of time")
