#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb")
def hbnb():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template(
        "100-hbnb.html", states=states, amenities=amenities, places=places
    )


@app.teardown_appcontext
def teardown(err):
    """teardown app context"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
