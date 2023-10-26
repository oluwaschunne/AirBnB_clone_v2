#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

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
    return "C {}".format(text.replace("_", " "))


@app.route("/python/(<text>)", strict_slashes=False)
def pyt(text="is_cool"):
    """return message"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def numm(n):
    """return message"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numm2(n):
    """return message"""
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
