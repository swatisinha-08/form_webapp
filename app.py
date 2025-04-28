from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = {
            "firstname": request.form.get("Firstname"),
            "lastname": request.form.get("lastname"),
            "password": request.form.get("pwd"),
            "gender": request.form.get("Gender"),
            "email": request.form.get("email")
        }
        # Here you can save to database / file / etc.
        return f"Form submitted successfully: {data}"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
