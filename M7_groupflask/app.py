from flask import Flask, render_template, request, session
import random
import ipaddress

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Function to reset attempts
def reset_attempts():
    session["attempts"] = 3

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# Binary to Decimal route
@app.route("/binary_to_decimal", methods=["GET", "POST"])
def binary_to_decimal():
    if "attempts" not in session:
        reset_attempts()

    if "binary_question" not in session or request.method == "POST":
        session["binary_question"] = format(random.randint(0, 255), '08b')
        reset_attempts()

    binary_question = session["binary_question"]
    correct_answer = int(binary_question, 2)

    result = None
    if request.method == "POST":
        user_answer = request.form["decimal_answer"]

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            result = "Correct!"
            session["binary_question"] = None
        else:
            session["attempts"] -= 1
            if session["attempts"] == 0:
                result = f"Wrong! Correct: {correct_answer}"
                session["binary_question"] = None
            else:
                result = f"Incorrect! You have {session['attempts']} attempts left."

    return render_template("binary_to_decimal.html", question=binary_question, result=result)

# Decimal to Binary route
@app.route("/decimal_to_binary", methods=["GET", "POST"])
def decimal_to_binary():
    if "attempts" not in session:
        reset_attempts()

    if "decimal_question" not in session or request.method == "POST":
        session["decimal_question"] = random.randint(0, 255)
        reset_attempts()

    decimal_question = session["decimal_question"]
    correct_answer = format(decimal_question, '08b')

    result = None
    if request.method == "POST":
        user_answer = request.form["binary_answer"]

        if user_answer == correct_answer:
            result = "Correct!"
            session["decimal_question"] = None
        else:
            session["attempts"] -= 1
            if session["attempts"] == 0:
                result = f"Wrong! Correct: {correct_answer}"
                session["decimal_question"] = None
            else:
                result = f"Incorrect! You have {session['attempts']} attempts left."

    return render_template("decimal_to_binary.html", question=decimal_question, result=result)

# Wildcard Mask Determination route
@app.route("/wildcard_mask", methods=["GET", "POST"])
def wildcard_mask():
    if "attempts" not in session:
        reset_attempts()

    if "wildcard_question" not in session or request.method == "POST":
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
        cidr = random.randint(8, 30)
        network = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
        session["wildcard_question"] = {"ip": ip, "cidr": cidr, "wildcard": str(network.hostmask)}
        reset_attempts()

    wildcard_question = session["wildcard_question"]
    correct_answer = wildcard_question["wildcard"]

    result = None
    if request.method == "POST":
        user_answer = request.form["wildcard_answer"]

        if user_answer == correct_answer:
            result = "Correct!"
            session["wildcard_question"] = None
        else:
            session["attempts"] -= 1
            if session["attempts"] == 0:
                result = f"Wrong! Correct: {correct_answer}"
                session["wildcard_question"] = None
            else:
                result = f"Incorrect! You have {session['attempts']} attempts left."

    return render_template("wildcard_mask.html", question=wildcard_question, result=result)

# Classful Address Analysis route
@app.route("/classful_analysis", methods=["GET", "POST"])
def classful_analysis():
    result = None
    if request.method == "POST":
        ip = request.form["ip_address"]
        try:
            first_octet = int(ip.split(".")[0])
            if 0 <= first_octet <= 127:
                result = f"The IP address {ip} belongs to: Class A."
            elif 128 <= first_octet <= 191:
                result = f"The IP address {ip} belongs to: Class B."
            elif 192 <= first_octet <= 223:
                result = f"The IP address {ip} belongs to: Class C."
            elif 224 <= first_octet <= 239:
                result = f"The IP address {ip} belongs to: Class D (Multicast)."
            elif 240 <= first_octet <= 255:
                result = f"The IP address {ip} belongs to: Class E (Experimental)."
            else:
                result = "Invalid IP address."
        except ValueError:
            result = "Invalid IP address."

    return render_template("classful_analysis.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
