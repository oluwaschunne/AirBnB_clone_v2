#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """return message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return message"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def cfunc(text):
    """return message"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
