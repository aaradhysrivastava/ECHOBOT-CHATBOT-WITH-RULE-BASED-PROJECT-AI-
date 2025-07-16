🗣️ Unified Voice & Text ChatBot with GUI
This project is a simple rule-based chatbot built using Python that supports both text and voice interactions through a clean graphical user interface (GUI). It integrates speech recognition, wake-word detection, and text-to-speech to act as a lightweight virtual assistant.

📌 Features
💬 Chat via text or voice.

🎙️ Wake word detection: activates voice mode when hearing "voice".

🔈 Responds using text-to-speech.

🧠 Handles speech input using speech recognition.

🖼️ GUI built using Tkinter with scrollable conversation window.

👋 Say "bye" to exit the assistant.

🗂️ Project Structure
Copy
Edit
voice-chatbot/
├── chatbot.py
├── gui.py
├── voice_module.py
├── requirements.txt
└── README.md
⚙️ How It Works
🪟 Launches a Tkinter-based GUI for chat.

🗣️ When the word "voice" is detected in input, it enters voice mode.

🎤 Listens to the user's voice and processes it using speech_recognition.

🧠 Responds based on simple rule-based logic.

🔊 Uses pyttsx3 to speak responses aloud.

👂 Listens again or exits if the user says "bye".

🧪 Installation & Usage
🔧 Requirements
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Make sure you have a working microphone and speaker.

▶️ Run the Project
bash
Copy
Edit
python chatbot.py
You can switch between text and voice input. Just type or say "voice" to activate voice mode.

🔁 Example Output
bash
Copy
Edit
You: voice
(Chatbot switches to voice mode)

You (speaking): Hello
Bot (speaks): Hello! How can I help you?

You (speaking): bye
Bot (speaks): Goodbye!
🧠 Concepts Used
Rule-Based Logic

Wake Word Detection

Speech Recognition (speech_recognition)

Text-to-Speech (pyttsx3)

GUI Programming with Tkinter

👨‍💻 Author
Made using Python by [AARADHY SRIVASTAVA].
