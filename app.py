from flask import Flask, request

app = Flask(__name__)

# 🟢 UI Page
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>SG-AI</title>
        <style>
            body {
                font-family: sans-serif;
                background: #ece5dd;
                margin: 0;
            }

            .chat-box {
                max-width: 400px;
                margin: auto;
                padding: 10px;
                height: 90vh;
                overflow-y: auto;
            }

            .msg {
                display: flex;
                margin: 10px 0;
            }

            .user {
                justify-content: flex-end;
            }

            .bot {
                justify-content: flex-start;
            }

            .bubble {
                padding: 10px;
                border-radius: 10px;
                max-width: 70%;
            }

            .user .bubble {
                background: #dcf8c6;
            }

            .bot .bubble {
                background: white;
            }

            /* 🔵 SG LOGO */
            .logo {
                width: 26px;
                height: 26px;
                background: #1877f2;
                border-radius: 50%;
                margin-right: 6px;

                display: flex;
                align-items: center;
                justify-content: center;

                color: white;
                font-size: 11px;
                font-weight: 500;
                opacity: 0.9;
            }

            .input-box {
                position: fixed;
                bottom: 0;
                width: 100%;
                display: flex;
                background: white;
                padding: 10px;
            }

            input {
                flex: 1;
                padding: 10px;
            }

            button {
                padding: 10px;
            }
        </style>
    </head>

    <body>

        <div class="chat-box" id="chat"></div>

        <div class="input-box">
            <input id="msg" placeholder="Type message...">
            <button onclick="sendMsg()">Send</button>
        </div>

        <script>
            function addMessage(text, type) {
                let chat = document.getElementById("chat");

                let msgDiv = document.createElement("div");
                msgDiv.className = "msg " + type;

                // 🔵 BOT LOGO
                if (type === "bot") {
                    let logo = document.createElement("div");
                    logo.className = "logo";
                    logo.innerText = "SG";
                    msgDiv.appendChild(logo);
                }

                let bubble = document.createElement("div");
                bubble.className = "bubble";
                bubble.innerText = text;

                msgDiv.appendChild(bubble);
                chat.appendChild(msgDiv);

                chat.scrollTop = chat.scrollHeight;
            }

            function sendMsg() {
                let input = document.getElementById("msg");
                let text = input.value;

                if (!text) return;

                addMessage(text, "user");
                input.value = "";

                fetch("/msg?text=" + encodeURIComponent(text))
                .then(res => res.text())
                .then(data => {
                    addMessage(data, "bot");
                });
            }
        </script>

    </body>
    </html>
    """

# 🟢 Bot logic
@app.route("/msg")
def msg():
    user = request.args.get("text")

    if not user:
        return "Message pampu bro"

    text = user.lower().strip()
    text = text.replace("?", "").replace(".", "")

    if "name" in text or "who are you" in text or "nee peru" in text:
        return "Naa peru SG-AI-12 bro 🤖"

    elif "hi" in text or "hello" in text or "hey" in text:
        return "Hello bro 😄"

    elif "how are you" in text:
        return "Nenu bagunnanu bro 🔥 nuvvu?"

    else:
        return "Ardham kaledhu bro 😅"


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
