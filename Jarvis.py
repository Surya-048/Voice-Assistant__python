import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import os
import random
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon")
    elif(hour>=17 and hour<19):
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am Zira Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 50
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
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

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('suryguddu248@gmail.com', 'Senapati@123')
    server.sendmail('suryguddu248@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    # speak("surya is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\all_music'
            songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[random(0,len(songs)-1)]))
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))

            # os.startfile(os.path.join(music_dir,songs[0]))
        elif 'play movie' in query:
            movie_dir = 'D:\\Movie'
            movies = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movies[random.randint(0, len(movies)-1)]))


        elif 'the time' in query:
            srtTime = datetime.datetime.now().strftime( "%H:%M:%S")
            speak(f"Sir, the time is {srtTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\unkno\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif 'email to surya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "senapatibhimasen481@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Surya,I am not able to send this email")


        elif 'quite' in query:
            exit()  