# SWE_HW1_2023 by Natanan Nithiittikrai 6380852
## Vending Machine Tracking Application

### Products
Components: product_id (unique), name, quantity

- Get all products
- Get a product's components based from id
- Delete a product
- Create a product
- Edit the product quantity

### Location 
Components: location_id, location_name

- Get all location
- Get a listing of product based on the machine id
- Delete a location
- Create a new location
- Edit the location name

### Movement
Components: prod_name, from_loc, to_loc, quantity

- Move Un-allocated Product to any Machine location
- Move allocated product from one machine to another machine location

### Requirement
`pip install flask`
### How to test
`flask run`
