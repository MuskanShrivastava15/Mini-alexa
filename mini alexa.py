import pyttsx3    #pip install pyttsx3
import speech_recognition as sr   #pip install Speech recognition sr is pet name
import datetime
import wikipedia
import webbrowser
import os
import smtplib


yantra = pyttsx3.init('sapi5')
voices = yantra.getProperty('voices')
# print(voices[0].id)
yantra.setProperty('voice',voices[1].id)


def speak(audio):
    yantra.say(audio)
    yantra.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Mini alexa... ! Please tell me how may I help You")

def takecommand():
     r = sr.Recognizer()       #Itt takes microphone input from the user and returns string output
     with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
         print("Recognizing...")
         query=r.recognize_google(audio, language='en-IN')
         print(f"User said:{query}\n")

     except Exception as e:
         #print(e)

         print("Say that again please....")
         return "None"
     return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dvnshmlvi@gmail.com', '82680000')
    server.sendmail('dvnshmlvi@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishme()
    while True:
    #if 1:
        query = takecommand().lower()

    # Logic for exicuting task based on query
        if 'wikipedia' in query:
            speak('searchng Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2) #how many sentece depend on you
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'your name' in query:
            speak("I am Dev...!  and your name")

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open translator' in query:
            webbrowser.open('www.googletranslator.com')


        elif 'play music' in query:
            music_dir='C:\\Users\\user\\Desktop\\Desktop folders\\after_servo\\New folder (2)'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
            print(strTime)

        elif 'open code' in query:
           codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

        elif 'pycharm' in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.4\\bin\\pycharm64.exe"
            os.startfile(pycharm)

        elif 'full name' in query:
            speak("My name is muskan shrivastav....!")

        elif 'make you' in query:
            speak('div makes me')

        elif 'old are you' in query:
            speak('I am 2 days old')

        elif 'meet you' in query:
            speak('nice to meet you')

        elif'send email' in query:
            try:
                speak("What should i say")
                content=takecommand()
                to="cs171064@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")


        elif 'stop' in query:
            speak("Thank you so much...!")
            speak("Have a nice day.....!")
            exit()