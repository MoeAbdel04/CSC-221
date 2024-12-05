from flask import Flask, render_template, request, redirect, url_for, flash
from menu_functions import (
    binary_to_decimal_game,
    decimal_to_binary_game,
    classful_address_analysis,
    wildcard_mask_determination,
    save_results,
)

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/binary_to_decimal", methods=["GET", "POST"])
def binary_to_decimal():
    if request.method == "POST":
        user_answer = request.form["user_answer"]
        result = binary_to_decimal_game(user_answer)
        flash(result, "info")
        return redirect(url_for("binary_to_decimal"))
    return render_template("binary_to_decimal.html")

@app.route("/decimal_to_binary", methods=["GET", "POST"])
def decimal_to_binary():
    if request.method == "POST":
        user_answer = request.form["user_answer"]
        result = decimal_to_binary_game(user_answer)
        flash(result, "info")
        return redirect(url_for("decimal_to_binary"))
    return render_template("decimal_to_binary.html")

@app.route("/classful_analysis", methods=["GET", "POST"])
def classful_analysis():
    if request.method == "POST":
        ip_address = request.form["ip_address"]
        result = classful_address_analysis(ip_address)
        flash(result, "info")
        return redirect(url_for("classful_analysis"))
    return render_template("classful_analysis.html")

@app.route("/wildcard_mask", methods=["GET", "POST"])
def wildcard_mask():
    if request.method == "POST":
        user_answer = request.form["user_answer"]
        result = wildcard_mask_determination(user_answer)
        flash(result, "info")
        return redirect(url_for("wildcard_mask"))
    return render_template("wildcard_mask.html")

@app.route("/results")
def results():
    save_results()
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)
