import datetime
import speech_recognition as sp
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sp.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace("jarvis", "")
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The time now is" + time)
    elif "wikipedia, what, who, why" in command:
        person = command.replace("wikipedia, what, who, why", "")
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)
    elif "game" in command:
        talk("Sorry I am an AI")
    elif "friends" in command:
        talk("Sorry Sir!")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please repeat as you were not clear")


while True:
    run_jarvis()
