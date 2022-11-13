from pathlib import Path
from unittest import mock

from project.app import app, init_db

@mock.patch("project.app.hello", return_value="Hello, World!", autoSpec=True)
def test_index(mock_hello):
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_database():
    init_db()
    assert Path("crafty_danes.db").is_file()