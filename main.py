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
        api_key = "c2d53de70ac9fb9b8788a4ab41dda26ec1da0128d203828ce6bc81a60835eec5"

        url = f"https://serpapi.com/search.json?q={query}&api_key={api_key}"
        res = requests.get(url).json()

        if "organic_results" in res:
            results = res["organic_results"][:3]

            answers = []
            for r in results:
                title = r.get("title", "")
                snippet = r.get("snippet", "")
                answers.append(f"{title}\n{snippet}")

            return "\n\n".join(answers)

        return "Result dorakaledhu bro 😅"

    except:
        return "Search error bro 😅"

# =========================
# 🤖 REPLY
# =========================
def generate_reply(msg):
    msg = msg.lower()

    # custom replies
    if "hi" in msg:
        return "Hello bro 😎"

    # 🔥 fallback to search
    result = search_online(msg)
    return result

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
