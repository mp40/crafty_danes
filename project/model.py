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

def get_beer_by_id():
    return 'beer'