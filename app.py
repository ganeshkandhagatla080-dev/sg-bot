from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "<h1>SG Bot Live 🔥</h1><p>Welcome bro 😄</p>"

# Test route
@app.route("/test")
def test():
    return "Working perfectly bro ✅"

# Message route (input test)
@app.route("/msg")
def msg():
    user = request.args.get("text")
    return f"You said: {user}"

# Run app (important for local + Railway fallback)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
