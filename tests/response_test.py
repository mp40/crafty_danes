from project.app import app
from project.model import get_beers

from seed_beers import seed_beers

class Cursor:
    def fetchall():
        return seed_beers

class DB:
    def execute(query):
        return Cursor

    def close():
        return

def test_beers():
    ctx = app.app_context()
    ctx.push()
    result = get_beers()

    assert result == seed_beers
