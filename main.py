from flask import Flask, request, jsonify
import json, os
import requests
import time

app = Flask(__name__)

# 🌐 Online Search (Improved)
def search_online(query):
    try:
        url = "https://serpapi.com/search"
        params = {
            "q": query,
            "api_key": "YOUR_API_KEY"
        }
        res = requests.get(url, params=params).json()

        if "organic_results" in res:
            return res["organic_results"][0]["snippet"]
        else:
            return "Search lo dorakaledhu bro 😅"
    except:
        return "Search error bro 😓"


# 🧠 Brain Logic
def brain_reply(msg, brain):
    # ✅ Memory check
    if msg in brain:
        return brain[msg]

    # ✅ Basic replies
    if "hi" in msg:
        return "Hello bro 😎"
    elif "siri" in msg:
        return "😏 Siri garu topic aa?"
    elif "how are you" in msg:
        return "Super bro 😄 nuvvu ela unnav?"

    # 🌐 Online fallback
    return search_online(msg)


# 🏠 Home Route
@app.route("/")
def home():
    return "S-GPT Running 🔥"


# 💬 Chat API (POST method)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    msg = data.get("message", "").lower()
    user_id = data.get("uid", "default")

    FILE = f"brain_{user_id}.json"

    # 📂 Load memory
    brain = {}
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                brain = json.load(f)
        except:
            brain = {}

    # 🧠 Get reply
    reply = brain_reply(msg, brain)

    # 💾 Save learning
    brain[msg] = reply
    with open(FILE, "w") as f:
        json.dump(brain, f)

    # ⏳ Small delay (typing feel)
    time.sleep(0.5)

    return jsonify({"reply": reply})


# ▶ Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # trigger update v2
