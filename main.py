import json
import os

file = "brain.json"

# Load brain
if os.path.exists(file):
    with open(file, "r") as f:
        brain = json.load(f)
else:
    brain = {}

# Normalize (spelling fix)
def normalize(text):
    text = text.lower()
    text = text.replace("th", "t")
    text = text.replace("aa", "a")
    return text

print("SG Smart Bot 🤖 ready bro")
print("Commands: bye, list, forget")

while True:
    user = normalize(input("You: "))

    # Exit
    if user == "bye":
        print("Bot: Bye bro 👋")
        break

    # List learned
    if user == "list":
        print("Bot learned:", list(brain.keys()))
        continue

    # Reset
    if user == "forget":
        brain.clear()
        with open(file, "w") as f:
            json.dump(brain, f)
        print("Bot: reset ayindi bro 😅")
        continue

    # 🔴 Siri special (balanced & respectful)
    if "siri" in user and "love" in user:
        print("Bot: slow ga vellali bro… respect maintain chey ❤️")
        continue

    elif "siri" in user:
        print("Bot: 😏 Siri garu topic ante careful bro… comfort important")
        continue

    # 🟢 SG natural replies
    if "ela unnav" in user or "how are you" in user:
        print("Bot: Nenu bagunna bro 😎 nuvvu ela unnav?")
        continue

    elif "em chesthunav" in user or "what are you doing" in user:
        print("Bot: Nitho matladuthunna bro 🤖")
        continue

    elif "thinnava" in user:
        print("Bot: Thinna bro 😄 nuvvu thinnava?")
        continue

    elif "tired" in user or "alasipoya" in user:
        print("Bot: Konchem rest thisuko bro… over avvakudadhu 💪")
        continue

    elif "work" in user or "money" in user:
        print("Bot: Focus bro 💸 slow ga build cheddam")
        continue

    elif "love" in user:
        print("Bot: fast ga kaadu bro… respect + patience important ❤️")
        continue

    elif "miss" in user:
        print("Bot: 😏 evarini miss avthunnav bro?")
        continue

    elif "alone" in user:
        print("Bot: Nuvvu alone kaadu bro 🤝 nenu unna")
        continue

    elif "bored" in user:
        print("Bot: Oka chai teesukoni relax avvu bro ☕")
        continue

    elif "night" in user:
        print("Bot: late avvakunda paduko bro 😴 health important")
        continue

    # Greeting
    if any(word in user for word in ["hi", "hello", "hey"]):
        print("Bot: Hello bro 😎")
        continue

    found = False

    # Smart match
    for key in brain:
        if normalize(key) in user:
            print("Bot:", brain[key])
            found = True
            break

    # Learning
    if not found:
        print("Bot: Nak teliyadhu bro 😅 naku nerpinchu")
        reply = input("You (teach me): ")

        brain[user] = reply

        with open(file, "w") as f:
            json.dump(brain, f)

        print("Bot: Nerchukunna bro 🔥")
