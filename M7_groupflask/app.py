from flask import Flask, render_template, request, redirect, url_for, flash
from menu_functions import save_results
import random
import ipaddress

app = Flask(__name__)
app.secret_key = "super_secret_key_for_session_management"  # Replace with a strong, random string

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/binary_to_decimal", methods=["GET", "POST"])
def binary_to_decimal():
    # Generate a random binary question
    question = format(random.randint(0, 255), '08b')
    result = None

    if request.method == "POST":
        user_answer = request.form["user_answer"]
        correct_answer = int(question, 2)
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            result = "Correct!"
        else:
            result = f"Wrong! The correct answer is {correct_answer}."
        flash(result, "info")
        # Generate a new question for the next round
        question = format(random.randint(0, 255), '08b')

    return render_template("binary_to_decimal.html", question=question, result=result)

@app.route("/decimal_to_binary", methods=["GET", "POST"])
def decimal_to_binary():
    # Generate a random decimal question
    question = random.randint(0, 255)
    result = None

    if request.method == "POST":
        user_answer = request.form["user_answer"]
        correct_answer = format(question, '08b')
        if user_answer == correct_answer:
            result = "Correct!"
        else:
            result = f"Wrong! The correct answer is {correct_answer}."
        flash(result, "info")
        # Generate a new question for the next round
        question = random.randint(0, 255)

    return render_template("decimal_to_binary.html", question=question, result=result)

@app.route("/classful_analysis", methods=["GET", "POST"])
def classful_analysis():
    result = None

    if request.method == "POST":
        ip_address = request.form["ip_address"]
        try:
            first_octet = int(ip_address.split('.')[0])
            if 0 <= first_octet <= 127:
                ip_class = "Class A"
            elif 128 <= first_octet <= 191:
                ip_class = "Class B"
            elif 192 <= first_octet <= 223:
                ip_class = "Class C"
            elif 224 <= first_octet <= 239:
                ip_class = "Class D (Multicast)"
            elif 240 <= first_octet <= 255:
                ip_class = "Class E (Experimental)"
            else:
                ip_class = "Invalid IP"
            result = f"The IP address {ip_address} belongs to: {ip_class}."
        except Exception as e:
            result = f"Error: {e}"
        flash(result, "info")

    return render_template("classful_analysis.html", result=result)

@app.route("/wildcard_mask", methods=["GET", "POST"])
def wildcard_mask():
    # Generate random IP and CIDR
    random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
    random_cidr = random.randint(8, 30)
    ip_with_cidr = f"{random_ip}/{random_cidr}"
    result = None

    if request.method == "POST":
        user_answer = request.form["user_answer"]
        try:
            network = ipaddress.ip_network(ip_with_cidr, strict=False)
            correct_wildcard = str(network.hostmask)
            if user_answer == correct_wildcard:
                result = "Correct!"
            else:
                result = f"Wrong! The correct Wildcard Mask is {correct_wildcard}."
        except ValueError as e:
            result = f"Invalid input: {e}"
        flash(result, "info")
        # Generate a new random IP and CIDR for the next round
        random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
        random_cidr = random.randint(8, 30)
        ip_with_cidr = f"{random_ip}/{random_cidr}"

    return render_template("wildcard_mask.html", ip_with_cidr=ip_with_cidr, result=result)

@app.route("/results")
def results():
    save_results()
    flash("Results have been saved successfully!", "success")
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)
