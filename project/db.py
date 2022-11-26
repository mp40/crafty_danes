import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from seed_beers import seed_beers


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
   

    db.cursor()

    data = [
        (1, seed_beers[0]['name'], seed_beers[0]['brewery'], seed_beers[0]['abv'], seed_beers[0]['type'], seed_beers[0]['receptacle_size'], seed_beers[0]['receptacle_type']),
        (2, seed_beers[1]['name'], seed_beers[1]['brewery'], seed_beers[1]['abv'], seed_beers[1]['type'], seed_beers[1]['receptacle_size'], seed_beers[1]['receptacle_type']),
        (3, seed_beers[2]['name'], seed_beers[2]['brewery'], seed_beers[2]['abv'], seed_beers[2]['type'], seed_beers[2]['receptacle_size'], seed_beers[2]['receptacle_type']),
        (4, seed_beers[3]['name'], seed_beers[3]['brewery'], seed_beers[3]['abv'], seed_beers[3]['type'], seed_beers[3]['receptacle_size'], seed_beers[3]['receptacle_type']),
        (5, seed_beers[4]['name'], seed_beers[4]['brewery'], seed_beers[4]['abv'], seed_beers[4]['type'], seed_beers[4]['receptacle_size'], seed_beers[4]['receptacle_type']),
        (6, seed_beers[5]['name'], seed_beers[5]['brewery'], seed_beers[5]['abv'], seed_beers[5]['type'], seed_beers[5]['receptacle_size'], seed_beers[5]['receptacle_type']),
    ]
    db.executemany("INSERT INTO beers VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')        

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)    