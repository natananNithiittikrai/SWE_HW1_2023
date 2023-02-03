import sqlite3
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

    # def test_location_removal(self):
    #     # First, add a new location
    #     data = {"location_name": "Test Location to Remove"}
    #     requests.post(self.url, data=data, allow_redirects=True)
    #
    #     # Then, remove the added location
    #     data = {"location_name": "Test Location to Remove"}
    #     response = requests.post(self.url, data=data, allow_redirects=True)
    #
    #     # Check if the removal was successful
    #     self.assertEqual(response.status_code, 200)
    #     # Test fetching products from the database
    #     db = sqlite3.connect("inventory.sqlite")
    #     cursor = db.cursor()
    #
    #     cursor.execute("SELECT * FROM location")
    #     locations = cursor.fetchall()
    #     self.assertEqual(len(locations), 4)
    #
    #     # Clean up the database
    #     cursor.execute("DELETE FROM location")
    #     db.commit()


if __name__ == "__main__":
    unittest.main()
