import datetime
import pyttsx3  # type: ignore
import wikipedia # type: ignore
import webbrowser
import os
import speech_recognition as sr # type: ignore

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
     speak("Good Morning Boss")

    elif hour >= 12 and hour <= 18:
       speak("Good Afternoon Boss")

    elif hour >=18 and hour <= 20:
        speak("Good Evening Boss")

    else:
        speak("Good night Boss")

    speak("Friday Here , What I have to Do now")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
        print("Finished listening.")
    
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
        except Exception as e:
            print(f"Error occurred: {e}")
            return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  # type: ignore
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()  # type: ignore
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtbe ' in query:
              webbrowser.open("youtube.com")

        elif 'play music' in query:

            music_dir = 'D:\\cool minded\\songs\\Favorite Songs2'

            os.makedirs(music_dir, exist_ok=True)

            songs = os.listdir(music_dir)

    
            print(f"Directory created at: {music_dir}")
            print(songs)  # type: ignore

            if songs:
              os.startfile(os.path.join(music_dir, songs[0]))  # type: ignore
            else:
              print("No songs found in the directory.")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strTime}")
       
        elif 'quit' in query:
            speak("Ok boss!")
            break
