import speech_recognition as sr
import webbrowser

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print(source)
# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
    if "python" in r.recognize_google(audio):
        url = "https://www.python.org/"
        webbrowser.open(url)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
