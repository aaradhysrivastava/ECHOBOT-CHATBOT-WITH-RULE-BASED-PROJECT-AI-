<!DOCTYPE html>

  <h1>🗣️ Unified Voice & Text ChatBot with GUI</h1>
  <p>This project is a simple rule-based chatbot built using Python that supports both <strong>text</strong> and <strong>voice interactions</strong> through a clean graphical user interface (GUI). It integrates speech recognition, wake-word detection, and text-to-speech to act as a lightweight virtual assistant.</p>

  <h2>📌 Features</h2>
  <ul>
    <li>💬 Chat via text or voice.</li>
    <li>🎙️ Wake word detection: activates voice mode when hearing <code>"voice"</code>.</li>
    <li>🔈 Responds using text-to-speech.</li>
    <li>🧠 Handles speech input using <code>speech_recognition</code>.</li>
    <li>🖼️ GUI built using Tkinter with scrollable conversation window.</li>
    <li>👋 Say <code>"bye"</code> to exit the assistant.</li>
  </ul>

  <h2>🗂️ Project Structure</h2>
  <div class="folder-structure">
    voice-chatbot/<br>
    ├── main.py<br>
    ├── requirements.txt<br>
    └── README.md
  </div>

  <h2>⚙️ How It Works</h2>
  <ul>
    <li>Launches a Tkinter-based GUI for chat.</li>
    <li>When the word <code>"voice"</code> is detected, it enters voice mode.</li>
    <li>Listens to the user's voice via microphone.</li>
    <li>Processes voice input using speech recognition and responds with rules.</li>
    <li>Say <code>"bye"</code> to exit voice mode.</li>
  </ul>

  <h2>🧪 Installation & Usage</h2>
  <h3>🔧 Requirements</h3>
  <p>Install dependencies:</p>
  <pre><code>pip install -r requirements.txt</code></pre>
  <p>Ensure you have a working microphone and speaker.</p>

  <h3>▶️ Run the Project</h3>
  <pre><code>python main.py</code></pre>
  <p>Type or say <code>"voice"</code> to activate voice mode.</p>

  <h2>🔁 Example Output</h2>
  <pre>
You: voice
(Chatbot switches to voice mode)
You (speaking): Hello
Bot (speaks): Hello! How can I help you?
You (speaking): bye
Bot (speaks): Goodbye!
  </pre>

  <h2>🧠 Concepts Used</h2>
  <ul>
    <li>Rule-Based Logic</li>
    <li>Wake Word Detection</li>
    <li>Speech Recognition (<code>speech_recognition</code>)</li>
    <li>Text-to-Speech (<code>pyttsx3</code>)</li>
    <li>GUI Programming with Tkinter</li>
  </ul>

  <h2>👨‍💻 Author</h2>
  <p>Made using Python by <strong>Aaradhy Srivastava</strong>.</p>

</body>
</html>
