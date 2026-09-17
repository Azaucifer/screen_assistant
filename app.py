from dotenv import load_dotenv
from database import get_messages, init_db, save_message
from flask import Flask, render_template, request
from google import genai
from google.genai import types
import markdown
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

init_db()

history = []

for message in get_messages():
    role = "user" if message[1] == "user" else "model"

    history.append(
        types.Content(
            role=role,
            parts=[types.Part(text=message[2])],
        )
    )


chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    history=history,
)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")

        save_message("user", question)

        response = chat.send_message(question)
        response = response.text

        save_message("assistant", response)

    messages = get_messages()

    formatted_messages = []

    for message in messages:
        if message[1] == "assistant":
            content = markdown.markdown(message[2], extensions=["fenced_code"])
        else:
            content = message[2]

        formatted_messages.append(
            (message[0], message[1], content)
        )

    return render_template(
        "index.html",
        messages=formatted_messages,
    )


if __name__ == "__main__":
    app.run(debug=True)