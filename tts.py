import pyttsx3

def speak(text):
    # Initialize the TTS engine with espeak
    engine = pyttsx3.init(driverName='espeak')
    
    # Optionally set properties like volume and speaking rate
    engine.setProperty('rate', 150)  # Speed of speech (default: 200)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Set the voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Use the first available voice
    print(f"Vision AI : {text}")
    
    # Convert the text to speech
    engine.say(text)
    
    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    # Example text input for TTS
    text = "Hello, welcome to the Raspberry Pi text to speech program."
    
    # Call the text_to_speech function
    print(text)
    speak(text)
