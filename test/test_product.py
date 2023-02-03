import unittest

import requests


class TestProduct(unittest.TestCase):
    URL = "http://127.0.0.1:5000/product"
    def test_product_creation(self):
        # Test adding a new product
        data = {"prod_name": "Test Product", "prod_quantity": "100"}
        response = requests.post(self.URL, data=data, allow_redirects=True)
        # Check if the product was added successfully
        self.assertEqual(response.status_code, 200)

    def test_product_name_empty(self):
        data = {"prod_name": "", "prod_quantity": ""}
        response = requests.post(self.URL, data=data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
