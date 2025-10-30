import sys
import requests

API_URL = "http://127.0.0.1:5000/chat"


def send_message(message: str) -> str:
    try:
        resp = requests.post(API_URL, json={"message": message}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if "reply" in data:
            return data["reply"]
        return data.get("error", "Unexpected response from server.")
    except requests.exceptions.ConnectionError:
        return "Cannot reach server at 127.0.0.1:5000. Is it running?"
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Terminal Chat Client (type 'exit' to quit)")
    while True:
        try:
            message = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if message.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        reply = send_message(message)
        print(reply)


if __name__ == "__main__":
    sys.exit(main())
