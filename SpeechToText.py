import speech_recognition

# Obtain some audio from the mic

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

# Recognise audio with google speech recognition
print("You said: ")
print(recognizer.recognize_google(audio))