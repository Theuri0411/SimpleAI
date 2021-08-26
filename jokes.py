import pyjokes as pj
import pyttsx3 as py

command = input("Type J for a joke: ")

engine = py.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

    if "joke" "j" "funny" in command:
        print(pj.get_jokes())
        talk(pj.get_jokes())
    else:
        print("no request made")
        talk("No request made")
