import unittest
import requests

class DeleteTestCase(unittest.TestCase):
    def test_delete(self):
        # Test location deletion
        response = requests.get("http://127.0.0.1:5000/delete?type=location&loc_id=9", allow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Test product deletion
        response = requests.get("http://127.0.0.1:5000/delete?type=product&prod_id=9", allow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
