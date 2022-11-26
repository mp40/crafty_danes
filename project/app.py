from flask import jsonify
from . import create_app

from project.model import hello, get_beers

app = create_app()

@app.route("/")
def res():
    return hello()

@app.route('/beers')
def beers():
    beers = get_beers()
    return jsonify(beers)

if __name__ == "__main__":
    app.run()