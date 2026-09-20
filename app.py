from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

body {
    margin: 0;
    background: #343541;
    font-family: Arial;
    color: white;
}

.chat {
    padding: 10px;
    max-width: 700px;
    margin: auto;
    margin-bottom: 70px;
}

.msg {
    padding: 12px;
    margin: 8px;
    border-radius: 10px;
    animation: fadeIn 0.3s ease-in;
}

.user {
    background: #10a37f;
    text-align: right;
}

.bot {
    background: #444654;
    text-align: left;
}

.input-box {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: #40414f;
    display: flex;
}

input {
    flex: 1;
    padding: 12px;
    border: none;
    outline: none;
    font-size: 16px;
}

button {
    padding: 12px;
    background: #10a37f;
    color: white;
    border: none;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
</head>

<body>

<div class="chat" id="chat"></div>

<div class="input-box">
<input id="msg" placeholder="Ask anything bro...">
<button onclick="sendMsg()">Send</button>
</div>

<script>

let chatDiv = document.getElementById("chat");

function addMsg(text, cls) {
    let div = document.createElement("div");
    div.className = "msg " + cls;
    div.innerText = text;
    chatDiv.appendChild(div);
    chatDiv.scrollTop = chatDiv.scrollHeight;
}

function showTyping() {
    let div = document.createElement("div");
    div.className = "msg bot";
    div.id = "typing";
    div.innerText = "typing...";
    chatDiv.appendChild(div);
    chatDiv.scrollTop = chatDiv.scrollHeight;
}

function removeTyping() {
    let t = document.getElementById("typing");
    if (t) t.remove();
}

function typeEffect(text) {
    let div = document.createElement("div");
    div.className = "msg bot";
    chatDiv.appendChild(div);

    let i = 0;
    let interval = setInterval(() => {
        div.innerText += text[i];
        i++;
        chatDiv.scrollTop = chatDiv.scrollHeight;
        if (i >= text.length) clearInterval(interval);
    }, 20);
}

function sendMsg() {
    let input = document.getElementById("msg");
    let msg = input.value;
    if (!msg) return;

    addMsg(msg, "user");
    input.value = "";

    showTyping();

    fetch("/chat?msg=" + msg)
    .then(res => res.json())
    .then(data => {
        removeTyping();
        typeEffect(data.reply);
    });
}

// ENTER key send
document.getElementById("msg").addEventListener("keypress", function(e){
    if(e.key === "Enter"){
        sendMsg();
    }
});

</script>

</body>
</html>
"""

@app.route("/chat")
def chat():
    msg = request.args.get("msg", "").lower()

    if "hi" in msg:
        reply = "Hello bro 🔥 ela unnav?"
    elif "siri" in msg:
        reply = "👀 Siri garu gurinchi alochisthunnava bro 😏"
    elif "love" in msg:
        reply = "slow ga vellali bro… respect important ❤️"
    else:
        reply = "Hmm bro 🤔 inkonchem cheppu"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
