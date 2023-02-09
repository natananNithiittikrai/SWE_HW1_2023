import sqlite3
from unittest import mock

import pytest

from app import app


def test_movement1():
    # test GET request
    response = app.test_client().get("/movement")
    assert response.status_code == 200

    # test POST request with complete data
    # response = app.test_client().post(
    #     '/movement',
    #     data={"prod_name": "Green Tea", "from_loc": "MUIC Old building", "to_loc": "location1", "quantity": "10"}
    # )
    # assert response.status_code == 500
    # assert b"Transaction added successfully" in response.data

    # test POST request with missing from_loc data
    # response = app.test_client().post(
    #     '/movement',
    #     data={"prod_name": "product12", "to_loc": "location2", "quantity": "10"}
    # )
    # assert response.status_code == 302
    # assert b"Transaction added successfully" in response.data

    # mock sqlite3.connect to raise an error
    with mock.patch("sqlite3.connect") as mock_connect:
        mock_connect.side_effect = sqlite3.Error("Error connecting to database")
        response = app.test_client().post(
            "/movement",
            data={
                "prod_name": "product12",
                "from_loc": "location1",
                "to_loc": "location2",
                "quantity": "10",
            },
        )
        assert response.status_code == 500
