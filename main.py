import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import re
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def chatbot_response(user_input):
    user_input = user_input.lower()

    patterns = {
        r"\bhello\b|\bhi\b": "Hello! How can I help you today?",
        r"how are you": "I'm just a program, but I'm doing fine! How about you?",
        r"your name": "I'm ChatBot, your virtual assistant.",
        r"help": "Sure, I'm here to help! Please tell me your issue.",
        r"time": f"Current time is {datetime.now().strftime('%H:%M:%S')}",
        r"bye": "Goodbye! Have a great day!",
        r"thank": "You're welcome!"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    return "I'm not sure how to respond to that. Can you rephrase?"

# Global wake word
WAKE_WORD = "voice"

def voice_assistant():
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Voice assistant activated. Say 'bye' to exit.\n")
    chat_window.config(state=tk.DISABLED)
    speak("Voice assistant activated. Say bye to exit.")

    while True:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Listening for wake word...\n")
        chat_window.config(state=tk.DISABLED)

        text = listen(timeout=5, phrase_time_limit=3)
        if text == "":
            speak("Sorry, I didn't catch that.")
            continue

        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You (voice): {text}\n")
        chat_window.config(state=tk.DISABLED)

        if WAKE_WORD in text:
            speak("I am listening.")
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, "Listening for command...\n")
            chat_window.config(state=tk.DISABLED)

            command = listen(timeout=5, phrase_time_limit=5)
            if command == "":
                speak("Sorry, I didn't catch that.")
                continue

            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"You (voice): {command}\n")
            chat_window.config(state=tk.DISABLED)

            if "bye" in command:
                speak("Goodbye!")
                chat_window.config(state=tk.NORMAL)
                chat_window.insert(tk.END, "Voice assistant stopped.\n")
                chat_window.config(state=tk.DISABLED)
                break

            response = chatbot_response(command)
            speak(response)
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"ChatBot: {response}\n")
            chat_window.config(state=tk.DISABLED)

def send_text():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    entry.delete(0, tk.END)

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_text}\n")
    chat_window.config(state=tk.DISABLED)

    if user_text.lower() == "bye":
        response = "Goodbye!"
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"ChatBot: {response}\n")
        chat_window.config(state=tk.DISABLED)
        speak(response)
        root.quit()
        return

    response = chatbot_response(user_text)
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"ChatBot: {response}\n")
    chat_window.config(state=tk.DISABLED)
    speak(response)

def start_voice_thread():
    voice_thread = threading.Thread(target=voice_assistant, daemon=True)
    voice_thread.start()

# --- GUI Setup ---

root = tk.Tk()
root.title("Unified ChatBot with Voice Activation & GUI")

chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=70, height=20, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10)

# Instruction note
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "NOTE: To activate voice assistant, say ' my voice'. To exit voice mode, say ' my bye'.\n\n")
chat_window.config(state=tk.DISABLED)

entry = tk.Entry(root, width=55)
entry.pack(padx=10, pady=(0, 10))
entry.focus()

send_button = tk.Button(root, text="Send Text", command=send_text)
send_button.pack(side=tk.LEFT, padx=(10,5), pady=(0,10))

voice_button = tk.Button(root, text="Activate Voice Assistant", command=start_voice_thread)
voice_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

root.mainloop()
