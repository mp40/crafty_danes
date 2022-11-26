from unittest import mock

from project.app import app
from seed_beers import seed_beers

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, Beers!"

@mock.patch("project.app.get_beers", return_value=seed_beers, autoSpec=True)
def test_beers(mock_get_beers):
    request = app.test_client()
    response = request.get("/beers")

    assert response.status_code == 200
    assert response.json == seed_beers
