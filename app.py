from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import pathlib

# === BASE PATHS ===
# Define the project directory and message storage file
BASE_DIR = pathlib.Path(__file__).parent
STORAGE = BASE_DIR / "storage" / "data.json"

# Create a Flask application
app = Flask(__name__)


# === ROUTE: MAIN PAGE ===
@app.get("/")
def index():
    # Give the template index.html
    return render_template("index.html")


# === ROUTE: MESSAGE SEND FORM (GET) ===
@app.get("/message")
def message_form():
    # Submit the message.html form
    return render_template("message.html")


# === ROUTE: FORM PROCESSING (POST) ===
@app.post("/message")
def message_submit():

    # Getting data from the form
    username = request.form.get("username", "")
    message = request.form.get("message", "")

    # Read existing messages from JSON
    try:
        with open(STORAGE, "r", encoding="utf-8") as f:
            saved = json.load(f)
    except:
        saved = {}  # If the file does not exist, we create an empty dictionary

    # Create a timestamp and add a new message
    timestamp = str(datetime.now())
    saved[timestamp] = {"username": username, "message": message}

    # Save the updated JSON
    with open(STORAGE, "w", encoding="utf-8") as f:
        json.dump(saved, f, indent=4, ensure_ascii=False)

    # Redirect to the message reading page
    return redirect("/read")


# === ROUTE: READ ALL MESSAGES ===
@app.get("/read")
def read_messages():
    # Read messages from a file
    try:
        with open(STORAGE, "r", encoding="utf-8") as f:
            messages = json.load(f)
    except:
        messages = {}

    # Sort by time (keys), newest on top
    sorted_messages = dict(sorted(messages.items(), key=lambda x: x[0], reverse=True))

    # Pass messages to the read.html template
    return render_template("read.html", messages=sorted_messages)


# === 404 ERROR HANDLER ===
@app.errorhandler(404)
def page_not_found(e):
    # Give the error.html template for a 404 error
    return render_template("error.html"), 404


# === LAUNCHING THE APPLICATION ===
if __name__ == "__main__":
    # Run Flask on port 3000
    app.run(host="0.0.0.0", port=3000)
