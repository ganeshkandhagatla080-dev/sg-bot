from flask import Flask, request

app = Flask(__name__)

@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    # clean text
    text = user.lower().strip()
    text = text.replace("?", "").replace(".", "")

    # 🔴 Name (important - top lo undali)
    if "name" in text or "who are you" in text or "nee peru" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    # Greetings
    elif "hi" in text or "hello" in text or "hey" in text:
        return "Hello bro 😄"

    # How are you
    elif "how are you" in text:
        return "Nenu bagunnanu bro 🔥 nuvvu?"

    # Default
    else:
        return "Ardham kaledhu bro 😅"


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
