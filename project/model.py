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
    db = get_db()
    beer = db.execute('SELECT * FROM beers WHERE id = ?;', [id]).fetchall()
    db.close()

    return dict(beer[0])

def post_beer(beer):
    name = beer["name"]
    brewery = beer["brewery"]
    abv = beer["abv"]
    type = beer["type"]
    receptacle_size = beer["receptacle_size"]
    receptacle_type = beer["receptacle_type"]

    db = get_db()
    db.execute('INSERT INTO beers (name, brewery, abv, type, receptacle_size, receptacle_type) VALUES(?, ?, ?, ?, ?, ?);', [name, brewery, abv, type, receptacle_size, receptacle_type])
    new_beer = db.execute('SELECT * FROM beers ORDER BY id DESC LIMIT 1').fetchall()
    db.commit()
    db.close()

    return dict(new_beer[0])    

def delete_beer_by_id(id):
    db = get_db()
    db.execute('DELETE FROM beers WHERE id = ?;', [id])
    db.commit()
    db.close()

    return None  

def put_beer_by_id(id, beer):
    name = beer["name"]
    brewery = beer["brewery"]
    abv = beer["abv"]
    type = beer["type"]
    receptacle_size = beer["receptacle_size"]
    receptacle_type = beer["receptacle_type"]

    db = get_db()
    db.execute('UPDATE beers SET name = ?, brewery = ?, abv = ?, type = ?, receptacle_size = ?, receptacle_type = ? WHERE id = ?;', [name, brewery, abv, type, receptacle_size, receptacle_type, id])
    updated_beer = db.execute('SELECT * FROM beers WHERE id = ?', [id]).fetchall()
    db.commit()
    db.close()

    return dict(updated_beer[0])