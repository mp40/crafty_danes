from project.app import app
from project.model import get_beers, get_beer_by_id, post_beer, delete_beer_by_id, put_beer_by_id

from project.db import init_db

from seed_beers import seed_beers

def test_get_beers():
    ctx = app.app_context()
    ctx.push()
    init_db()

    result = get_beers()

    assert result == seed_beers

def test_get_beer_by_id():
    ctx = app.app_context()
    ctx.push()
    init_db()

    result = get_beer_by_id('1')

    assert result == seed_beers[0]

def test_post_beer():
    ctx = app.app_context()
    ctx.push()
    init_db()

    new_beer = {
        "name": "D's Nuts",
        "brewery":"To Øl",
        "abv": 12.0,
        "type": "Imperial Stout",
        "receptacle_size": 375,
        "receptacle_type": "bottle"
    }

    inserted_beer = {
        "id": 7,
        "name": "D's Nuts",
        "brewery":"To Øl",
        "abv": 12.0,
        "type": "Imperial Stout",
        "receptacle_size": 375,
        "receptacle_type": "bottle"
    }

    result = post_beer(new_beer)

    assert result == inserted_beer

def test_delete_beer_by_id():
    ctx = app.app_context()
    ctx.push()
    init_db()

    result = delete_beer_by_id(1)

    assert result == None

def test_put_beer_by_id():
    ctx = app.app_context()
    ctx.push()
    init_db()

    beer = {
        "id": 1,
        "name": "Pink XXXX & Unicorns",
        "brewery":"Amager Bryghus",
        "abv": 4.6,
        "type": "IPL",
        "receptacle_size": 500,
        "receptacle_type": "can"
    }

    result = put_beer_by_id(1, beer) 

    assert result == beer