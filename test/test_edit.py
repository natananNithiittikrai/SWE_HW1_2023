import unittest
import requests

class TestEditEndpoint(unittest.TestCase):
    # def test_edit_location(self):
    #     url = "http://127.0.0.1:5000/edit?type=location"
    #     data = {"loc_id": "1", "loc_name": "Test Location"}
    #     response = requests.post(url, data=data, allow_redirects=True)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.headers["Location"], "http://127.0.0.1:5000/location")

    def test_edit_location(self):
        url = "http://127.0.0.1:5000/edit?type=location"
        pre_data = {"loc_id": "8", "loc_name": "Test Location"}
        response = requests.post(url, data=pre_data, allow_redirects=True)
        self.assertEqual(pre_data.get('loc_name'), "Test Location")
        self.assertEqual(response.status_code, 200)

        after_data = {"loc_id": "8", "loc_name": "Changed Location 1"}
        response = requests.post(url, data=after_data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(pre_data.get('loc_name'), after_data.get('loc_name'))

        # Extract location name from the response content
        response_data = response.json()
        actual_loc_name = response_data.get('loc_name')

        # Compare the extracted location name to the expected location name
        self.assertEqual(actual_loc_name, after_data.get('loc_name'))

    def test_edit_product(self):
        url = "http://127.0.0.1:5000/edit?type=product"
        pre_data = {"prod_id": "5", "prod_name": "Test Product", "prod_quantity": "10"}
        response = requests.post(url, data=pre_data, allow_redirects=True)
        self.assertEqual(pre_data.get('prod_name'), "Test Product")
        self.assertEqual(pre_data.get('prod_quantity'), "10")
        self.assertEqual(response.status_code, 200)

        after_data = {"prod_id": "5", "prod_name": "Changed Product", "prod_quantity": "20"}
        response = requests.post(url, data=after_data, allow_redirects=True)
        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(pre_data.get('prod_name'), after_data.get('prod_name'))
        self.assertNotEqual(pre_data.get('prod_quantity'), after_data.get('prod_quantity'))

        # Extract location name from the response content
        response_data = response.json()
        actual_loc_name = response_data.get('loc_name')

        # Compare the extracted location name to the expected location name
        self.assertEqual(actual_loc_name, after_data.get('loc_name'))


if __name__ == "__main__":
    unittest.main()
