from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")
        response = f"You asked: {question}"
        return render_template("index.html", question=question, response=response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)