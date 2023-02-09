import sqlite3
from unittest import mock

from app import app


def test_edit():
    endpoint = "/edit?type=location"

    # Test location type POST request
    response = app.test_client().post(
        endpoint, data={"loc_id": 1, "loc_name": "new_location_name"}
    )
    assert response.status_code == 200

    # test POST request with type location and missing data
    response = app.test_client().post(
        "/edit?type=location", data={"loc_id": "1", "loc_name": ""}
    )
    assert response.status_code == 200

    # assert response.get_json().get("loc_id") == 1
    # assert response.get_json().get("loc_name") == "new_location_name"

    # Test product type POST request
    # response = app.test_client().post(
    #     '/edit?type=product',
    #     data={"prod_id": 6, "prod_name": "Pringles", "prod_quantity": 120}
    # )
    # assert response.status_code == 302

    # test POST request with type product and missing data
    # response = app.test_client().post('/edit?type=product', data={"prod_id": "1", "prod_name": "", "prod_quantity": ""})
    # assert response.status_code == 302

    # test GET request with unknown type
    response = app.test_client().get("/edit?type=unknown")
    assert response.status_code == 500

    # Test product type POST request with error
    with mock.patch("sqlite3.connect") as mock_connect:
        mock_connect.side_effect = sqlite3.Error("Error connecting to database")
        response = app.test_client().post(
            "/edit?type=product",
            data={"prod_id": 1, "prod_name": "new_product_name", "prod_quantity": 20},
        )
        assert response.status_code == 500
