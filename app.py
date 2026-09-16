from dotenv import load_dotenv
from database import get_messages, init_db, save_message
from flask import Flask, render_template, request
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")

        save_message("user", question)

        response = chat.send_message(question)
        response = response.text

        save_message("assistant", response)

    messages = get_messages()

    return render_template(
        "index.html",
        messages=messages,
    )


if __name__ == "__main__":
    app.run(debug=True)