Run the chatbot program:
  python main.py
Use the GUI window to type messages or click Activate Voice Assistant and say " my voice" to start talking by voice.
Say "my bye" to exit voice assistant mode or close the app window.


Dependencies
Python 3.x
tkinter (usually included with Python)
SpeechRecognition
pyttsx3
pyaudio (for microphone input)

Notes
Ensure your microphone is connected and working.
Voice recognition uses Google’s Web Speech API, so internet connection is required.
Installing pyaudio can be tricky on some systems:
On Windows, you can install from unofficial wheels (e.g., via https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
On Linux/macOS, you may need to install portaudio development headers first (sudo apt-get install portaudio19-dev on Ubuntu).
The chatbot currently recognizes basic commands — you can extend it by adding more patterns in the code.

Project Structure
project-folder/
│
├── main.py           # Chatbot script with GUI and voice assistant
├── requirements.txt  # List of required Python packages
└── README.md         # This file

