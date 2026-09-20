from flask import Flask, request

app = Flask(__name__)

# memory
chat_history = []

# clear route
@app.route("/clear")
def clear():
    global chat_history
    chat_history = []
    return "<h3>Chat cleared bro ✅</h3><a href='/'>Back</a>"

@app.route("/")
def home():
    msg = request.args.get("msg", "")
    reply = ""

    if msg:
        user = msg.lower()

        if "hi" in user:
            reply = "Hello bro 🔥 ela unnav?"
        elif "siri" in user:
            reply = "👀 Siri garu gurinchi alochisthunnava bro 😏"
        elif "love" in user:
            reply = "slow ga vellali bro… respect important ❤️"
        else:
            reply = "Hmm interesting bro 🤔 inkonchem cheppu"

        chat_history.append(("You", msg))
        chat_history.append(("Bot", reply))

    chat_html = "<ul>"
    for sender, text in chat_history:
        chat_html += f"<li><b>{sender}:</b> {text}</li>"
    chat_html += "</ul>"

    return f"""
    <h2>SG Bot 🤖</h2>

    <form method="get">
        <input name="msg" placeholder="Type message">
        <button type="submit">Send</button>
    </form>

    <br>
    <a href="/clear"><button>Clear Chat</button></a>

    {chat_html}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
