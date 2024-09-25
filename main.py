import time
import os
from tts import speak
from stt import listen
from assistant import generate_response
from capture import capture_image
from lens_assistant import generate_image_response

def assistant_loop():
    speak("Assistant Opened")
    while True:
        prompt = listen()
        if prompt == "close":
            speak("Closing Assistant")
            break
        response = generate_response(prompt)
        speak(response)

def smart_lens_loop():
    speak("Smart lens active")
    while True:
        prompt = listen()
        if prompt == "close":
            speak("Closing Smart Lens")
            break
        image_path = capture_image()
        if image_path:
            response = generate_image_response(prompt, image_path)
            speak(response)
        else:
            speak("Failed to capture image. Please try again.")

def main():
    speak("Hi. I am VisionAI")
    speak("How can I help you?")
    
    while True:
        command = listen()
        if command == "open assistant":
            assistant_loop()  # Call the assistant loop
        elif command == "open smart lens":
            smart_lens_loop()  # Call the smart lens loop
        elif command == "close":
            speak("Closing program")
            break
        else:
            speak("I did not capture any input. Please try again.")

if __name__ == "__main__":
    main()
