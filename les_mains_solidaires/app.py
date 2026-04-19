from unicodedata import name

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "lesmains-solidaires-secret"  # Change this in production


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if name and email and message:
        # TODO: send email / save to DB
        flash("Merci pour votre message ! Nous vous répondrons bientôt.", "success")
    else:
        flash("Veuillez remplir tous les champs.", "error")

    return redirect(url_for("index") + "#contact")


if __name__ == "main":
    app.run(debug=True)
