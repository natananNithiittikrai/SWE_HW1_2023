import sqlite3
import unittest
from unittest.mock import patch

from app import app, summary


class SummaryTestCase(unittest.TestCase):
    def test_get_request(self):
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)

    # @patch('sqlite3.connect')
    # def test_fetch_data(self, mock_connect):
    #     # mock the cursor object
    #     mock_cursor = mock_connect.return_value.cursor.return_value
    #     # set the return value of the cursor execute method
    #     mock_cursor.execute.side_effect = [
    #         [(1, 'location1'), (2, 'location2')],
    #         [(1, 'product1', 10, 5), (2, 'product2', 20, 15)],
    #         [(1, 'product1', 5), (2, 'product2', 5)]
    #     ]
    #
    #     result = summary()
    #     self.assertEqual(result.link, None)
    #     self.assertEqual(result.title, "Summary")
    #     self.assertEqual(result.locations, [(1, 'location1'), (2, 'location2')])
    #     self.assertEqual(result.products, [(1, 'product1', 10, 5), (2, 'product2', 20, 15)])
    #     self.assertEqual(result.database, [(1, 'product1', 5), (2, 'product2', 5)])
    #
    # @patch('sqlite3.connect')
    # def test_fetch_data_exception(self, mock_connect):
    #     mock_connect.return_value.cursor.return_value.execute.side_effect = sqlite3.Error("Test error")
    #
    #     result = summary()
    #     self.assertEqual(result.link, None)
    #     self.assertEqual(result.title, "Summary")
    #     self.assertEqual(result.locations, None)
    #     self.assertEqual(result.products, None)
    #     self.assertEqual(result.database, None)
