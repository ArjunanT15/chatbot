# ChatBuddy — Simple Flask Chatbot

A minimal web-based rule‑driven chatbot built with Flask. Type a message and the bot replies based on simple keyword rules.

## Features
- **Web UI** with input box and send button
- **Rule-based replies** implemented in `chatbot.py`
- **Lightweight API** endpoint at `/get?msg=...`
- **Static assets and Jinja template** served via Flask

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Vanilla JS

## Project Structure
```
chatbot web/
├─ app.py                 # Flask app, routes, server
├─ chatbot.py             # Rule-based response logic
├─ requirements.txt       # Python dependencies
├─ templates/
│  └─ index.html          # Main page
└─ static/
   └─ style.css           # Styles (if added)
```

## Prerequisites
- Python 3.8+

## Setup
1. (Optional) Create a virtual environment
   - Windows (PowerShell):
     - python -m venv .venv
     - .\.venv\Scripts\Activate.ps1
   - Windows (CMD):
     - python -m venv .venv
     - .\.venv\Scripts\activate.bat
2. Install dependencies
   - pip install -r requirements.txt

## Run the App
- Default dev server (from `app.py`):
  - The file contains two `app.run(...)` calls. Keep only one active to avoid conflicts. Recommended:
    - app.run(debug=True, host="127.0.0.1", port=5050)
- Start:
  - python app.py
- Open:
  - http://127.0.0.1:5050/ (or the host/port you configured)

## API
- GET `/get?msg=YOUR_TEXT`
  - Returns: JSON string response from the bot
  - Example: `/get?msg=hello`

## How It Works
- `app.py`
  - `/` renders `templates/index.html`
  - `/get` reads the `msg` query param and calls `chatbot_response`
- `chatbot.py`
  - Simple keyword matching on lowercased input

## Customize Responses
- Edit `chatbot.py`
  - Add new `elif` blocks for keywords
  - Adjust default fallback message in the final `else`

## Troubleshooting
- If the server won’t start or exits immediately:
  - Ensure only one `if __name__ == "__main__": app.run(...)` block is active in `app.py`.
- If the page loads but messages fail:
  - Check the browser console and Flask logs.
  - Verify network request to `/get` returns 200 OK and JSON.

## License
- MIT (or your preferred license)
