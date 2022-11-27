from flask import jsonify, request
from . import create_app

from project.model import hello, get_beers, get_beer_by_id, post_beer

app = create_app()

@app.route("/")
def res():
    return hello()

@app.route('/beers', methods=['GET'])
def beers():
    beers = get_beers()
    return jsonify(beers)

@app.route('/beers/<id>')
def beer(id):
    beer = get_beer_by_id(id)
    return jsonify(beer)    

@app.route('/beers', methods=['POST'])
def insert():
    beer = request.get_json()
    posted_beer = post_beer(beer)
    return jsonify(posted_beer)    

if __name__ == "__main__":
    app.run()