from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return "Hello bro 😄"
    elif "how are you" in text:
        return "Nenu bagunnanu bro 🔥 nuvvu?"
    elif "siri" in text:
        return "Siri garu topic aa 😏"
    else:
        return "Ardham kaledhu bro 😅"
