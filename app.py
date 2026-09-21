from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>

<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>

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
    white-space: pre-wrap;
    line-height: 1.5;
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

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();


// 👇 nee code
let chatDiv = document.getElementById("chat");

function sendMsg() {
   // existing code
}

</script>

<div class="chat" id="chat"></div>

<div class="input-box">
<input id="msg" placeholder="Ask anything bro...">
<button onclick="sendMsg()">Send</button>
</div>

<script>

const firebaseConfig = {
  apiKey: "AIzaSyCOOle74AFX1tWH7X_ESb1e2DXTA5MgHro",
  authDomain: "sg-bot-1e220.firebaseapp.com",
  projectId: "sg-bot-1e220",
  storageBucket: "sg-bot-1e220.firebasestorage.app",
  messagingSenderId: "925979796012",
  appId: "1:925979796012:web:1c73b590bd148405ce6789",
  measurementId: "G-0ZL0RXD3GZ"
};

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// 🔐 unique user id
let userId = localStorage.getItem("uid");

if (!userId) {
    userId = Date.now().toString(36) + Math.random().toString(36).substring(2);
    localStorage.setItem("uid", userId);
}

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
    input.focus();

    showTyping();

    fetch("/chat?msg=" + encodeURIComponent(msg) + "&uid=" + userId)
    .then(res => res.json())
    .then(data => {
        removeTyping();
        typeEffect(data.reply);
    });
}

// enter key send
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
    user_id = request.args.get("uid", "default")

    FILE = f"brain_{user_id}.json"
    LAST = f"last_{user_id}.txt"

    # safe load brain
    brain = {}
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                brain = json.load(f)
        except:
            brain = {}

    # load last question
    last_question = ""
    if os.path.exists(LAST):
        with open(LAST, "r") as f:
            last_question = f.read()

    # 🧠 teaching
    if msg.startswith("teach:"):
        answer = msg.replace("teach:", "").strip()

        if last_question:
            brain[last_question] = answer

            with open(FILE, "w") as f:
                json.dump(brain, f)

            return jsonify({"reply": "Nerchukunna bro 🔥"})
        else:
            return jsonify({"reply": "Em nerpinchalo ardham kaledhu bro 😅"})

    # 🧠 learned replies
    for key in brain:
        if key == msg or key in msg:
            return jsonify({"reply": brain[key]})

    # 💬 default replies
    if "hi" in msg:
        reply = "Hello bro 🔥 ela unnav?"
    elif "siri" in msg:
        reply = "👀 Siri garu gurinchi alochisthunnava bro 😏"
    elif "love" in msg:
        reply = "slow ga vellali bro… respect important ❤️"
    else:
        reply = "Nak teliyadhu bro 😅 naku nerpinchu (type: teach: your reply)"

        with open(LAST, "w") as f:
            f.write(msg)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
