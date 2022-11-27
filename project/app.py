from flask import jsonify
from . import create_app

from project.model import hello, get_beers, get_beer_by_id

app = create_app()

@app.route("/")
def res():
    return hello()

@app.route('/beers')
def beers():
    beers = get_beers()
    return jsonify(beers)

@app.route('/beers/<id>')
def beer(id):
    beer = get_beer_by_id()
    return jsonify(beer)    

if __name__ == "__main__":
    app.run()