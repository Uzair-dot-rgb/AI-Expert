import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
user_name = ""


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    return ""


def respond_to_command(command):
    if "hello" in command:
        speak(f"Hello {user_name}, how can I assist you today?")
    
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    
    elif "date" in command:
        today = datetime.now().date()
        speak(f"Today's date is {today}")
    
    elif "joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        joke = random.choice(jokes)
        speak(joke)
    
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I'm sorry, I don't understand that command.")


def main():
    speak("Voice assistant activated. Say something!")
    
    while True:
        command = get_audio()
        
        if command:
            respond_to_command(command)


if __name__ == "__main__":
        main()