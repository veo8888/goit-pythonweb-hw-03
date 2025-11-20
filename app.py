from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
STORAGE = BASE_DIR / "storage" / "data.json"

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/message")
def message_form():
    return render_template("message.html")


@app.post("/message")
def message_submit():

    username = request.form.get("username", "")
    message = request.form.get("message", "")

    try:
        with open(STORAGE, "r", encoding="utf-8") as f:
            saved = json.load(f)
    except:
        saved = {}

    timestamp = str(datetime.now())
    saved[timestamp] = {"username": username, "message": message}

    with open(STORAGE, "w", encoding="utf-8") as f:
        json.dump(saved, f, indent=4, ensure_ascii=False)

    return redirect("/read")


@app.get("/read")
def read_messages():
    try:
        with open(STORAGE, "r", encoding="utf-8") as f:
            messages = json.load(f)
    except:
        messages = {}

    sorted_messages = dict(sorted(messages.items(), key=lambda x: x[0], reverse=True))

    return render_template("read.html", messages=sorted_messages)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
