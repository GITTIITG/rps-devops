import os, random
from flask import Flask, render_template, request

app = Flask(__name__)
CHOICES = ["rock", "paper", "scissors"]

def decide(user, comp):
    if user == comp:
        return "tie"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "win"
    else:
        return "lose"

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    user_choice = None
    comp_choice = None
    if request.method == "POST":
        user_choice = request.form["choice"]
        comp_choice = random.choice(CHOICES)
        result = decide(user_choice, comp_choice)
    return render_template("index.html", user=user_choice, comp=comp_choice, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
