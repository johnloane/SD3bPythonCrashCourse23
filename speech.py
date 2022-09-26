import pyttsx3

engine = pyttsx3.init()
name = input("Please enter your name> ")
engine.say(f"Hello, {name}")
engine.runAndWait()