import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")

        response = chat.send_message(question)
        response = response.text

        return render_template("index.html", question=question, response=response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)