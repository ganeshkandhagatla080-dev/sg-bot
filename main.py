from flask import Flask, request, jsonify
import json, os, requests

app = Flask(__name__)

# =========================
# 🧠 MEMORY
# =========================
def load_brain(file):
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_brain(file, brain):
    with open(file, "w") as f:
        json.dump(brain, f)

# =========================
# 🌐 SEARCH
# =========================
def search_online(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
        res = requests.get(url).json()

        if res.get("AbstractText"):
            return res["AbstractText"]

        if res.get("Answer"):
            return res["Answer"]

        if res.get("RelatedTopics"):
            for item in res["RelatedTopics"]:
                if isinstance(item, dict) and item.get("Text"):
                    return item["Text"]

        return None
    except:
        return None

# =========================
# 🤖 REPLY
# =========================
def generate_reply(msg):
    msg = msg.lower().strip()

    if msg == "hi":
        return "Hello bro 😎 ela unnava?"

    if msg == "hello":
        return "Hey bro 🔥 em chesthunav?"

    if "who are you" in msg:
        return "Nenu SG Bot bro 🤖 neeku help cheyadaniki ready"

    if "siri" in msg:
        return "😏 Siri garu topic aa bro?"

    # 🌐 fallback search
    result = search_online(msg)

    if result:
        return f"{result}\n\n👉 Simple ga cheppali ante bro 😄"

    return "Hmm bro 🤔 naku clear ga teliyadhu 😅 nuv explain chesthava?"

# =========================
# 🚀 CHAT
# =========================
@app.route("/chat")
def chat():
    msg = request.args.get("msg", "")
    user_id = request.args.get("uid", "default")

    FILE = f"brain_{user_id}.json"

    brain = load_brain(FILE)

    if msg in brain:
        return jsonify({"reply": brain[msg]})

    reply = generate_reply(msg)

    brain[msg] = reply
    save_brain(FILE, brain)

    return jsonify({"reply": reply})

# =========================
# 🎤 VOICE
# =========================
@app.route("/voice", methods=["POST"])
def voice():
    data = request.json
    text = data.get("text", "")

    reply = generate_reply(text)
    return jsonify({"reply": reply})

# =========================
# 🏠 HOME
# =========================
@app.route("/")
def home():
    return "SG BOT RUNNING 🔥"

# =========================
# ▶ RUN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
