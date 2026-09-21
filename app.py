from flask import Flask, request

app = Flask(__name__)

# Simple memory (temporary)
memory = {}

@app.route("/")
def home():
    return "<h1>SG Bot Live 🔥</h1><p>Try /msg?text=na peru Ganesh</p>"

@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    # Save name
    if "na peru" in text:
        name = text.replace("na peru", "").strip()
        if name:
            memory["name"] = name
            return f"Okay {name} 😊 gurthupettukunna"
        else:
            return "Mee peru cheppu bro 😄"

    # Recall name
    elif "na peru enti" in text:
        if "name" in memory:
            return f"Nuvvu {memory['name']} kadha 😄"
        else:
            return "Naku inka telidhu bro 😅"

    # Greetings
    elif "hi" in text or "hello" in text or "hey" in text:
        return "Hello bro 😄"

    # Identity
    elif "name" in text or "who are you" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    else:
        return "Ardham kaledhu bro 😅"

# Run app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
