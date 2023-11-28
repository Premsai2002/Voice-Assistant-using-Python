import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return None

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "how are you" in command:
        speak("I'm doing well, thank you!")
    elif "what is your name" in command:
        speak("I am a Python voice assistant.")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your Python voice assistant.")
    
    while True:
        command = listen()
        if command:
            process_command(command)
