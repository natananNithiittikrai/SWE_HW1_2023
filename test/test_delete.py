from app import app


def test_delete():
    with app.test_client() as client:
        # Test for location delete
        client.get("/delete?type=location&loc_id=1")
        result = client.get("/location")
        assert b"Location 1" not in result.data

        # Test for product delete
        client.get("/delete?type=product&prod_id=1")
        result = client.get("/product")
        assert b"Product 1" not in result.data
