import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #pip install smtplib
import pyjokes #pip install pyjoke

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print()
        print("Listening...")
        print()
        # r.pause_threshold = 1
        audio = r.listen(source,10,5)

    try:
        print("Recognizing...")
        print()    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        print()
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your id', to, content)
    server.close()

print()
print("Hello Sir!. Please tell me how may I help you ?")
speak(" Hello Sir!.")
wishMe()
speak("Please tell me how may I help you ?")

print()


while True:

    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        wresult = str(wikipedia.search(query, results = 1))
        results = wikipedia.summary(wresult, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'what is my name' in query:
        print("Your Name is Keshav Swami")
        speak("Your Name is Keshav Swami")

    elif 'how are you' in query:
        print("I am Fine Sir ! What can i do for you")
        speak("I am Fine Sir ! What can i do for you")

    elif 'what is your name' in query:
        print("My name is Shiwi Sir your Assistant !")
        speak("My name is Shiwi Sir. your Assistant !")

    elif 'when is my birthday' in query:
        strDate = datetime.date(1998, 3 , 10)
        print("The Date is : {0}".format(strDate))
        speak("The Date is {0}".format(strDate))

    elif 'where i am from' in query:
        print("You are from India, Chandigarh. The city beautiful")
        speak("You are from India, Chandigarh. The city beautiful")

    elif 'wish me happy birthday' in query:
        print('''"Happy Birthday to You
        " "Happy Birthday to You
        " "Happy Birthday " "Dear Keshu.
        " "Happy Birthday to You
        "''')
        speak('''"Happy Birthday to You
        " "Happy Birthday to You
        " "Happy Birthday " "Dear Keshu.
        " "Happy Birthday to You
        "''')

    elif 'open chrome' in query:
        chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        speak("Opening Google Chrome")
        print("Opening Google Chrome.......")
        os.startfile(chromePath)
    
    elif 'open youtube' in query:
        speak("Opening Youtube.com")
        print("Opening Youtube.com")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Opening google.com")
        print("Opening google.com")
        webbrowser.open("google.com")

    elif 'open stack overflow' in query:
        speak("Opening stackoverflow.com")
        print("Opening stackoverflow.com")
        webbrowser.open("stackoverflow.com") 

    elif 'open facebook' in query:
        speak("Opening Facebook.com")
        print("Opening Facebook.com")
        webbrowser.open("facebook.com")  


    elif 'play music' in query:
        music_dir = 'C://Users//swami//Music'
        songs = os.listdir(music_dir)
        print(songs)
        speak("Playing Music")    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif ('what is the time' in query) or ('time' in query):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The Time is : {0}".format(strTime))
        speak("The Time is {0}".format(strTime))

    elif 'open code' in query:
        codePath = "C:\\Users\\Rajat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS Code")
        print("Opening VS Code.......")
        os.startfile(codePath)

    elif 'tell me a joke' in query:
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
        speak(My_joke)

    elif ('send email' in query) or ('email' in query):
        try:
            speak("What should I send?")
            print("What should I send?")
            content = takeCommand()
            print()
            to = "rajatthakurk@gmail.com"
            sendEmail(to, content)
            print()
            speak("Email has been sent!")
            print("Email has been sent !")
            print()
        except Exception as e:
            print(e)
            speak("Sorry ,I am not able to send this email")  

    elif ('exit' in query) or ('bye bye' in query) or ('quit' in query):
        print("Bye Bye Sir ! See You Soon")
        speak("Bye Bye Sir ! See You Soon")

        exit()
