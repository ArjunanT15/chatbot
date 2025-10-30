from flask import Flask, request, jsonify

app = Flask(__name__)


def generate_response(message: str) -> str:
    msg = (message or "").strip().lower()

    if not msg:
        return "Please say something."
    if "arjun" in msg:
        return "Arjun is a software developer "


    if any(greet in msg for greet in ["hello", "hi", "hey","Arjun"]):
        return "Hello! How can I help you today?"

    if "help" in msg:
        return (
            "I am a simple terminal chat bot. Try: 'hello', 'help', or ask a short question. "
            "Type 'exit' in the client to quit."
        )

    if "your name" in msg or "who are you" in msg:
        return "I'm a minimal Flask chatbot running locally."
   
    return f"You said: {message}"


@app.get("/")
def health():
    return jsonify({"status": "ok"})


@app.post("/chat")
def chat():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message", "")
        reply = generate_response(message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Bind to localhost only; use default port 5000
    app.run(host="127.0.0.1", port=5000, debug=False)
