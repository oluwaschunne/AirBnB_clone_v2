#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """list all cities"""
    stored = storage.all(State)
    states = [state for key, state in stored.items()]
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(error):
    """teardown app context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
