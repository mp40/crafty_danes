import sqlite3

from flask import Flask, g

from project.db import hello, get_beers

# configuration
DATABASE = "crafty_danes.db"

# create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)

# connect to database
def connect_db():
    """Connects to the database."""
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

# create the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()

# open database connection
def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# close database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()

@app.route("/")
def res():
    return hello()

@app.route('/beers')
def beers():
    return get_beers()

if __name__ == "__main__":
    app.run()