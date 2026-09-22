from flask import Flask, request, jsonify, render_template
import requests, os, sqlite3

app = Flask(__name__)

# =========================
# 🧠 DATABASE (PERMANENT MEMORY)
# =========================
def init_db():
    conn = sqlite3.connect("brain.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS memory (msg TEXT, reply TEXT)")
    conn.commit()
    conn.close()

init_db()

def get_memory(msg):
    conn = sqlite3.connect("brain.db")
    c = conn.cursor()
    c.execute("SELECT reply FROM memory WHERE msg=?", (msg,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def save_memory(msg, reply):
    conn = sqlite3.connect("brain.db")
    c = conn.cursor()
    c.execute("INSERT INTO memory (msg, reply) VALUES (?, ?)", (msg, reply))
    conn.commit()
    conn.close()

# =========================
# 🌐 GOOGLE SEARCH (SerpAPI)
# =========================
def search_online(query):
    try:
        api_key = os.getenv("SERP_API_KEY") or "PASTE_YOUR_API_KEY"

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
# 🤖 REPLY LOGIC
# =========================
def generate_reply(msg):
    msg_lower = msg.lower()

    # simple replies
    if "hi" in msg_lower:
        return "Hello bro 😎"

    if "siri" in msg_lower:
        return "😏 Siri garu topic aa bro?"

    # search fallback
    result = search_online(msg)
    return result

# =========================
# 🚀 CHAT API
# =========================
@app.route("/chat")
def chat():
    msg = request.args.get("msg", "")
    
    # check memory
    reply = get_memory(msg)
    if reply:
        return jsonify({"reply": reply})

    # generate new
    reply = generate_reply(msg)

    # save memory
    save_memory(msg, reply)

    return jsonify({"reply": reply})

# =========================
# 🏠 HOME (UI later add cheddam)
# =========================
@app.route("/")
def home():
    return "SG BOT RUNNING 🔥"

# =========================
# ▶ RUN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
