import os
import sqlite3
import unittest

class TestInventoryApp(unittest.TestCase):
    DATABASE_NAME = 'test_inventory.sqlite'
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database', DATABASE_NAME),
    )
    client = app.test_client()

    def setUp(self):
        init_database()

    def tearDown(self):
        os.remove(self.DATABASE_NAME)

    def test_summary(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Summary', response.data)

    def test_product(self):
        response = self.client.get('/product')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product', response.data)

        response = self.client.post('/product', data={'prod_name': 'Test Product', 'prod_quantity': 10})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/product')

        # Verify that the product was added to the database
        db = sqlite3.connect(self.DATABASE_NAME)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products WHERE prod_name='Test Product'")
        product = cursor.fetchone()
        self.assertIsNotNone(product)
        self.assertEqual(product[1], 'Test Product')
        self.assertEqual(product[2], 10)

    def test_location(self):
        # Test adding a new location
        response = self.client.post('/location', data={'loc_name': 'Test Location'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/location')

        # Verify that the location was added to the database
        db = sqlite3.connect(self.DATABASE_NAME)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM location WHERE loc_name='Test Location'")
        location = cursor.fetchone()
        self.assertIsNotNone(location)
        self.assertEqual(location[1], 'Test Location')
        
    def test_movement(self):
        # Add a product and two locations to the database
        db = sqlite3.connect(self.DATABASE_NAME)
        cursor = db.cursor()
        cursor.execute("INSERT INTO products (prod_name, prod_quantity) VALUES ('Test Product', 10)")
        cursor.execute("INSERT INTO location (loc_name) VALUES ('Test Location 1')")
        cursor.execute("INSERT INTO location (loc_name) VALUES ('Test Location 2')")
        db.commit()

        # Test adding a new movement
        response = self.client.post('/movement', data={'prod_id': 1, 'from_loc_id': 1, 'to_loc_id': 2, 'prod_quantity': 5})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/movement')

        # Verify that the movement was added to the database
        cursor.execute("SELECT * FROM logistics WHERE prod_id=1 AND from_loc_id=1 AND to_loc_id=2 AND prod_quantity=5")
        movement = cursor.fetchone()
        self.assertIsNotNone(movement)


if __name__ == '__main__':
    unittest.main()

# For def init_database():
# It is not possible to test the init_database function as it is written in the code because it creates and 
# modifies the database, this should be handled carefully, it could be tested by creating a testing database and 
# comparing it's schema with the expected one after running the function.