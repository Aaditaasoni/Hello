from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/", methods=["Get", "Post"])
def home():
    result = None
    if request.method == "Post":
        try:
            number = int(request.form["number"])
            result = f"the number you entered is:{number}"

        except ValueError:
            result = "please enter a valid integer"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)