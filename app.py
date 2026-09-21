from flask import Flask, request

app = Flask(__name__)

memory = {}

@app.route("/")
def home():
    return "<h1>SG Bot Live 🔥</h1><p>Use /msg?text=name</p>"

@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    # Identity (fixed)
    if "name" in text or ("who" in text and "you" in text) or ("nee" in text and "peru" in text):
        return "Naa peru SG-AI-12 bro 🤖"

    # Teach
    if text.startswith("teach:"):
        try:
            content = text.replace("teach:", "").strip()
            q, a = content.split("=")
            memory[q.strip()] = a.strip()
            return "Okay bro 😊 nerchukunna"
        except:
            return "Format: teach: question = answer"

    # Memory
    if text in memory:
        return memory[text]

    # Greetings
    if "hi" in text or "hello" in text:
        return "Hello bro 😄"

    return "Naku telidhu bro 😅 naku nerpinchava?"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
