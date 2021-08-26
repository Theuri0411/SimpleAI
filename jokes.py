import pyjokes as pj
import pyttsx3 as py

command = input("Type joke for a joke: ")

engine = py.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if "joke" in command:
    print(pj.get_jokes())
    talk(pj.get_jokes())
elif "x" in command:
    print("stopped by user")
    talk("stopped by user")
else:
    print("No request made")
    talk("No request Made")
