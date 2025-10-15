from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Wczytanie zmiennych z .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # przykład użycia zmiennej z .env

@app.route("/")
def hello_world():
    return render_template("index01.html")

if __name__ == "__main__":
    app.run(debug=True)