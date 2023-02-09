import sqlite3
from unittest import mock

import pytest

from app import app

ENDPOINT = "http://127.0.0.1:5000/product"


def test_product():
    # test GET request
    response = app.test_client().get("/product")
    assert response.status_code == 200

    # test POST request
    response = app.test_client().post(
        "/product", data={"prod_name": "product12", "prod_quantity": "10"}
    )
    assert response.status_code == 302

    # test POST request with missing data
    response = app.test_client().post(
        "/product", data={"prod_name": "", "prod_quantity": ""}
    )
    assert response.status_code == 200

    # mock sqlite3.connect to raise an error
    with mock.patch("sqlite3.connect") as mock_connect:
        mock_connect.side_effect = sqlite3.Error("Error connecting to database")
        response = app.test_client().post(
            "/product", data={"prod_name": "product12", "prod_quantity": "10"}
        )
        assert response.status_code == 500

    # response = client.get(ENDPOINT)
    # print(response.data)
    # assert response.status_code == 200
    # Refractor code
    # Blueprint
    # Method database extract not in routes


# def test_product_GET():
#     response = requests.get(ENDPOINT)
#     assert response.status_code == 200
#     # assert "Products Log" in response.text
