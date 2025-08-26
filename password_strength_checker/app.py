from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character.")

    if strength == 5:
        return "Strong password 💪", []
    elif 3 <= strength < 5:
        return "Moderate password 🙂", remarks
    else:
        return "Weak password 😢", remarks

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    suggestions = []
    if request.method == "POST":
        password = request.form["password"]
        message, suggestions = check_password_strength(password)
    return render_template("index.html", message=message, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
