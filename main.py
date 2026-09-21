from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return "S-GPT Running 🔥"

@app.route("/chat")
def chat():
    msg = request.args.get("msg", "").lower()
    user_id = request.args.get("uid", "default")

    FILE = f"brain_{user_id}.json"

    brain = {}
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                brain = json.load(f)
        except:
            brain = {}

    if msg in brain:
        return jsonify({"reply": brain[msg]})

    if "hi" in msg:
        reply = "Hello bro 😎"
    elif "siri" in msg:
        reply = "😏 Siri garu topic aa?"
    else:
        reply = "Nak teliyadhu bro 😅"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
