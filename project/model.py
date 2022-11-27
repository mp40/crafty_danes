from project.db import get_db

def hello():
    return "Hello, Beers!"

def get_beers():

    db = get_db()
    beers = db.execute('SELECT * FROM beers;').fetchall()
    db.close()

    serialized_beers = []
    for beer in beers:
        serialized_beers.append(dict(beer))

    return serialized_beers

def get_beer_by_id(id):
    return 'beer'

def post_beer(beer):
    return 'posted beer'    

def delete_beer_by_id(id):
    return    

def put_beer_by_id(id):
    return 'updated beer'