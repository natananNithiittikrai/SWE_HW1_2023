import unittest

import requests


class TestLocation(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/location"

    def test_location_addition(self):
        data = {"location_name": "Test Location"}
        response = requests.post(self.url, data=data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_location_name_empty(self):
        data = {"location_name": ""}
        response = requests.post(self.url, data=data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
