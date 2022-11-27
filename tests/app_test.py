import json
from unittest import mock

from project.app import app
from seed_beers import seed_beers

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, Beers!"

@mock.patch("project.app.get_beers", return_value=seed_beers, autoSpec=True)
def test_get_beers(mock_get_beers):
    request = app.test_client()
    response = request.get("/beers")

    assert response.status_code == 200
    assert response.json == seed_beers

@mock.patch("project.app.get_beer_by_id", return_value=seed_beers[0], autoSpec=True)
def test_get_beer_by_id(mock_get_beer_by_id):
    request = app.test_client()
    response = request.get("/beers/1")

    mock_get_beer_by_id.assert_called_with('1')
    assert response.status_code == 200
    assert response.json == seed_beers[0]

@mock.patch("project.app.post_beer", return_value=seed_beers[0], autoSpec=True)
def test_post_beer(mock_post_beer):
    request = app.test_client()
    response = request.post(
        "/beers",    
        data=json.dumps(seed_beers[0]),
        headers={"Content-Type": "application/json"}
        )

    mock_post_beer.assert_called_with(seed_beers[0])
    assert response.status_code == 200
    assert response.json == seed_beers[0]

@mock.patch("project.app.delete_beer_by_id", return_value=None, autoSpec=True)
def test_delete_beer_by_id(mock_delete_beer_by_id):
    request = app.test_client()
    response = request.delete("/beers/1")
 
    mock_delete_beer_by_id.assert_called_with('1')
    assert response.status_code == 200

@mock.patch("project.app.put_beer_by_id", return_value=seed_beers[0], autoSpec=True)
def test_put_beer_by_id(mock_put_beer_by_id):
    request = app.test_client()
    response = request.put(
        "/beers/1",
        data=json.dumps(seed_beers[0]),
        headers={"Content-Type": "application/json"}
        )

    mock_put_beer_by_id.assert_called_with('1', seed_beers[0])
    assert response.status_code == 200
    assert response.json == seed_beers[0]    