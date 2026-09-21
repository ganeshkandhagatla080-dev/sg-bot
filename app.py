@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    # 🔴 Debug (temporary check)
    print("User said:", text)

    # ✅ Identity (strong match)
    if "name" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    if "who" in text and "you" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    if "nee" in text and "peru" in text:
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
