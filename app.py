@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    # Name (flexible)
    if "name" in text or "who are you" in text or "who r u" in text or "nee peru" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    # Greetings
    elif "hi" in text or "hello" in text or "hey" in text:
        return "Hello bro 😄"

    # How are you
    elif "how are you" in text:
        return "Nenu bagunnanu bro 🔥 nuvvu?"

    else:
        return "Ardham kaledhu bro 😅"
