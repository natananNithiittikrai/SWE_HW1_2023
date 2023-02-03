import unittest

import requests


class MovementTestCase(unittest.TestCase):
    def test_movement_post_request(self):
        url = "http://127.0.0.1:5000/movement"
        response = requests.post(
            url,
            data=dict(
                prod_name="Changed Product",
                from_loc="MUIC New Building",
                to_loc="Test Location",
                quantity="50",
            ),
            allow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual()
        # self.assertEqual(b"Transaction added successfully", response.data)

    def test_movement_unallocated_product(self):
        url = "http://127.0.0.1:5000/movement"
        data = {
            "prod_name": "Fanta",
            "from_loc": "",
            "to_loc": "Test Location",
            "quantity": "50",
        }
        response = requests.post(url, data=data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        product_name = response_data.get("prod_name")
        location = response_data.get("to_loc")
        self.assertEqual(product_name, data.get("prod_name"))
        # self.assertEqual(b"Transaction added successfully", response.data)

    def test_movement_post_request_with_invalid_data(self):
        response = self.app.post(
            "/movement",
            data=dict(prod_name="", from_loc="", to_loc="", quantity=""),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b"An error occurred", response.data)


if __name__ == "__main__":
    unittest.main()
