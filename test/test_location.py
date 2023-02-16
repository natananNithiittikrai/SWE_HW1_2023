import sqlite3
from unittest import mock

import pytest

from app import app


def test_location():
    app.config["WTF_CSRF_ENABLED"] = False
    # Test GET request
    response = app.test_client().get("/location")
    assert response.status_code == 200

    # Test POST request success
    response = app.test_client().post("/location", data={"location_name": "location1"})
    assert response.status_code == 302

    # Test POST request with SQLite error
    with mock.patch("sqlite3.connect") as mock_connect:
        mock_connect.side_effect = sqlite3.Error("Error connecting to database")
        response = app.test_client().post(
            "/location", data={"location_name": "location1"}
        )
        assert response.status_code == 500
