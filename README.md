# llm
This FastAPI application provides a WebSocket-based API endpoint (/ws/stream) that allows real-time evaluation of messages using a locally hosted AI model (like phi3 via Ollama).

#Step 1: Install Requirements
Make sure Python 3.7+ is installed, then install dependencies:

bash
Copy
Edit
pip install fastapi uvicorn requests
Step 2: Install and Run Ollama
If you haven’t already:

Install Ollama

Pull and run a model (e.g., phi3, llama3, mistral, etc.):

bash
Copy
Edit
ollama run phi3
This starts a local LLM server at http://localhost:11434.

 Step 3: Save Your App
Save the main.py code provided above in your project folder.

 Step 4: Start FastAPI Server
Run this command in your terminal:

bash
Copy
Edit
uvicorn main:app --reload
You’ll see logs like:

arduino
Copy
Edit
INFO:     Uvicorn running on http://127.0.0.1:8000

Step 5: Connect via WebSocket
You (or your frontend) can now connect to the WebSocket endpoint:

ws
Copy
Edit
ws://localhost:8000/ws/llm
Send any prompt text, and the LLM's response will stream back as chunks.
 Testing Options
Frontend:

js
Copy
Edit
const ws = new WebSocket("ws://localhost:8000/ws/llm");
ws.onmessage = (e) => console.log(e.data);
ws.onopen = () => ws.send("Explain quantum computing in simple terms.");
Browser Extension:
Use WebSocket King or Hoppscotch to test.

Python WebSocket Client (optional):
Ask if you want a CLI version in Python.
