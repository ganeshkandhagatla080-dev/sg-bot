from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "SG Bot Running 😎"

@app.route("/chat")
def chat():
    user = request.args.get("msg", "").lower()

    if "hi" in user:
        return "Hello bro 😎"
    elif "siri" in user:
        return "😏 Siri garu topic ante careful bro"
    else:
        return "Hmm bro interesting 🤔"

app.run(host="0.0.0.0", port=5000)
