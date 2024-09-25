import speech_recognition as sr
from sound import play_sound
import os

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the USB sound card as the microphone
    mic = sr.Microphone()

    with mic as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak into the microphone.")
        play_sound()
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        # Recognize the speech using Google's free API (you can use offline engines too)
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Error with the recognition service; {0}".format(e))

if __name__ == "__main__":
    listen()
