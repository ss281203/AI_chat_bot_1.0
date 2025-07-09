import speech_recognition as sr
import subprocess

def speak(text):
    print("[SPEAKING]:", text)
    subprocess.Popen(['say', text])

recognizer = sr.Recognizer()
mic = sr.Microphone()

speak("Hello! I am a simple AI voice chatbot. Say 'bye' to exit.")

while True:
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            user_input = recognizer.recognize_google(audio).lower()
            print(f"You: {user_input}")
        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            continue
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            continue
        except sr.RequestError:
            speak("API unavailable or quota exceeded.")
            continue

    if "bye" in user_input:
        speak("Goodbye! Have a nice day.")
        break
    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! How can I help you?")
    elif "weather" in user_input:
        speak("I can't check the weather yet, but I can chat with you!")
    elif "name" in user_input:
        speak("My name is Ai_chat_bot.1.0. What's yours?")
    
        
    else:
        speak("Sorry, I didn't understand that.")
