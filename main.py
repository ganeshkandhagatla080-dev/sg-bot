from flask import Flask, request, jsonify
import json, os
import requests

app = Flask(__name__)

# 🔍 Search function (simple)
def search_online(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(url).json()

        if res.get("AbstractText"):
            return res["AbstractText"]
        else:
            return "Online lo clear ga dorakaledhu bro 😅"
    except:
        return "Search error bro 😓"

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

    # ✅ Step 1: Memory check
    if msg in brain:
        return jsonify({"reply": brain[msg]})

    # ✅ Step 2: Basic replies
    if "hi" in msg:
        reply = "Hello bro 😎"
    elif "siri" in msg:
        reply = "😏 Siri garu topic aa?"

    # ✅ Step 3: Search online
    else:
        reply = search_online(msg)

        # ✅ Step 4: Save (auto learn)
        brain[msg] = reply
        with open(FILE, "w") as f:
            json.dump(brain, f)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
