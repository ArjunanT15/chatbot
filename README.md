# Flask Terminal Chatbot

A minimal Flask chat server with a simple terminal client.

## Features
- Simple rule-based responses in `app.py`
- JSON `/chat` endpoint
- Terminal client `cli_chat.py` that talks to the server

## Prerequisites
- Python 3.10+
- On Windows, these instructions assume you use WSL (Ubuntu) for terminal commands.

## Setup
```bash
# In WSL, navigate to the project directory
python3 -m venv .venv
source .venv/bin/activate 
for windows use 
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
# Terminal 1: start the Flask server
python app.py

# Terminal 2: start the terminal chat client
python cli_chat.py
```

## Test with curl (optional)
```bash
curl -s -X POST http://127.0.0.1:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "hello"}'
```

## Notes
- The bot is intentionally simple; extend `generate_response()` in `app.py` as needed.
- The server binds to `127.0.0.1:5000`. Change in `app.run(...)` if required.
"# ChatBot" 
"# Simple-chatbot" 
