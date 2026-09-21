from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "<h1>SG Bot Live 🔥</h1><p>Use /msg?text=hello</p>"

# Message route
@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    # Greetings
    if "hi" in text or "hello" in text or "hey" in text:
        return "Hello bro 😄"

    # How are you
    elif "how are you" in text:
        return "Nenu bagunnanu bro 🔥 nuvvu?"

    # Name / Identity
    elif "name" in text or "who are you" in text or "nee peru" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    # Siri topic
    elif "siri" in text:
        return "Siri garu topic aa 😏"

    # Default
    else:
        return "Ardham kaledhu bro 😅"

# Run app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
