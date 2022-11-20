from pathlib import Path
from unittest import mock
import json

from project.app import app, init_db
from seed_beers import seed_beers

@mock.patch("project.app.hello", return_value="Hello, World!", autoSpec=True)
def test_index(mock_hello):
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"

@mock.patch("project.app.get_beers", return_value=json.dumps(seed_beers), autoSpec=True)
def test_beers(mock_get_beers):
    request = app.test_client()
    response = request.get("/beers")

    assert response.status_code == 200
    assert response.data == bytes(json.dumps(seed_beers), encoding='utf8')


def test_database():
    init_db()
    assert Path("crafty_danes.db").is_file()    