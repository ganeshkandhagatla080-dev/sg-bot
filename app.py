from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>SG Bot 🤖</h2>
    <form action="/chat">
        <input name="msg" placeholder="Type message">
        <button type="submit">Send</button>
    </form>
    """

@app.route("/chat")
def chat():
    user = request.args.get("msg", "").lower()

    if "hi" in user:
        return "Hello bro 🔥 ela unnav?"
    elif "siri" in user:
        return "👀 Siri garu gurinchi alochisthunnava bro 😏"
    elif "love" in user:
        return "slow ga vellali bro… respect important ❤️"
    else:
        return "Hmm interesting bro 🤔 inkonchem cheppu"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
