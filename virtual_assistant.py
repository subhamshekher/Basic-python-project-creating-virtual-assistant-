import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            speak("unable to process")

    return said.lower()

def friday():
    if "how are you" in get_audio():
        speak("I am fine")
    if "Hi" in get_audio():
        speak("hello sir, hope you are doing fine")
    if "This is test one" in get_audio():
        speak("Test sucessfull")
    if "what's your name" in get_audio():
        speak("Hii this is friday your personal assistant")
    if "what time is it" in get_audio():
        speak(ctime())
    if "where is" in get_audio():
        said = said.split("")
        location = data[2]
        speak("Hang on sir , I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

WAKE = speak("hello sir")
print("Start")

while True:
    speak("Listening")
    text = get_audio()
    friday()

    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()
