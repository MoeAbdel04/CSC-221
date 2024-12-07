from flask import Flask, render_template, request, session
import random
import ipaddress

app = Flask(__name__)
app.secret_key = "super_secret_key_for_sessions"

# In-memory storage for results
results = {
    "binary_to_decimal": [],
    "decimal_to_binary": [],
    "classful_analysis": [],
    "wildcard_mask": []
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/binary_to_decimal", methods=["GET", "POST"])
def binary_to_decimal():
    if request.method == "GET":
        # Generate a new binary question
        question = format(random.randint(0, 255), '08b')  # 8-bit binary
        session["binary_question"] = question  # Save the new question in the session
        session["binary_correct_answer"] = int(question, 2)  # Save the correct answer in the session
        result = None  # No result to display for GET requests
    else:
        # Retrieve the stored question and correct answer from the session
        question = session.get("binary_question")
        correct_answer = session.get("binary_correct_answer")

        # Get the user's answer from the form
        user_answer = request.form["user_answer"]

        # Validate the user's input
        try:
            user_answer = int(user_answer)  # Convert input to integer
            if user_answer == correct_answer:
                result = "Correct!"
            else:
                result = f"Wrong! Correct: {correct_answer}"
        except ValueError:
            result = "Invalid input. Please enter a valid number."

        # Save the result to in-memory storage for display on the results page
        results["binary_to_decimal"].append({
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "result": result
        })

        # After a POST request, generate a new question for the next GET request
        question = format(random.randint(0, 255), '08b')  # Generate a new question
        session["binary_question"] = question  # Update the session with the new question
        session["binary_correct_answer"] = int(question, 2)  # Update the session with the new correct answer

    # Render the template with the current question and result
    return render_template("binary_to_decimal.html", question=question, result=result)


@app.route("/decimal_to_binary", methods=["GET", "POST"])
def decimal_to_binary():
    if request.method == "GET":
        # Generate a new decimal question
        question = random.randint(0, 255)  # Generate a random decimal number
        session["decimal_question"] = question  # Save the question in the session
        session["decimal_correct_answer"] = format(question, '08b')  # Calculate and save the correct binary answer
        result = None  # No result to display for GET requests
    else:
        # Retrieve the stored question and correct answer from the session
        question = session.get("decimal_question")
        correct_answer = session.get("decimal_correct_answer")

        # Get the user's answer from the form
        user_answer = request.form["user_answer"]

        # Validate the user's input
        if user_answer == correct_answer:
            result = "Correct!"
        else:
            result = f"Wrong! Correct: {correct_answer}"

        # Save the result to in-memory storage for display on the results page
        results["decimal_to_binary"].append({
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "result": result
        })

        # Generate a new question for the next GET request
        question = random.randint(0, 255)
        session["decimal_question"] = question
        session["decimal_correct_answer"] = format(question, '08b')

    # Render the template with the current question and result
    return render_template("decimal_to_binary.html", question=question, result=result)


@app.route("/classful_analysis", methods=["GET", "POST"])
def classful_analysis():
    ip_address = None
    result = None

    if request.method == "POST":
        # Get the user's input
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

        # Save the result to in-memory storage
        results["classful_analysis"].append({
            "ip_address": ip_address,
            "result": result
        })

    return render_template("classful_analysis.html", result=result)

@app.route("/wildcard_mask", methods=["GET", "POST"])
def wildcard_mask():
    if request.method == "GET":
        # Generate a random IP and CIDR, store it in the session
        random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
        random_cidr = random.randint(8, 30)
        ip_with_cidr = f"{random_ip}/{random_cidr}"
        correct_wildcard = str(ipaddress.ip_network(ip_with_cidr, strict=False).hostmask)
        session["wildcard_ip_with_cidr"] = ip_with_cidr
        session["wildcard_correct_answer"] = correct_wildcard
        result = None
    else:
        # Retrieve the stored IP with CIDR and correct wildcard mask from the session
        ip_with_cidr = session.get("wildcard_ip_with_cidr")
        correct_wildcard = session.get("wildcard_correct_answer")

        # Get the user's answer from the form
        user_answer = request.form["user_answer"]

        # Validate the user's input
        if user_answer == correct_wildcard:
            result = "Correct!"
        else:
            result = f"Wrong! Correct: {correct_wildcard}"

        # Save the result to in-memory storage
        results["wildcard_mask"].append({
            "ip_with_cidr": ip_with_cidr,
            "user_answer": user_answer,
            "correct_answer": correct_wildcard,
            "result": result
        })

    return render_template("wildcard_mask.html", ip_with_cidr=ip_with_cidr, result=result)

@app.route("/results")
def show_results():
    return render_template("results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
