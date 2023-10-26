#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
def states_ids(id):
    """list all states"""
    s_var = None
    stored = storage.all(State)
    for key, state in stored.items():
        if state.id == id:
            s_var = state
    return render_template("9-states.html", states=s_var, lst=False)


@app.route("/states", strict_slashes=False)
def states():
    """list all states"""
    stored = storage.all(State).items()
    state = [state for key, state in stored]
    return render_template("9-states.html", states=state, lst=True)


@app.teardown_appcontext
def teardown(error):
    """teardown app context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
