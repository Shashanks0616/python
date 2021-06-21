import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
           print("listening..")
           r.pause_threshold = 1
           audio = r.listen(source,timeout = 1,phrase_time_limit=5)


    try:
        print("Recognize....")
        query = r.recognize_google(audio,language = "en-in")

    except Exception as e:
        speak("Say that again plzz...")
        return "name" 
    return query


if __name__ == '__main__':
    # speak("maanya singh ")
    takeCommand()