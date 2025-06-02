# Coffee Shop Challenge

A Python project modeling a coffee shop system using object-oriented programming. The system includes customers, coffees, and orders, demonstrating many-to-many relationships.

## Setup Instructions
Clone the repository
git clone https://github.com/YOUR-USERNAME/coffee-shop-pythonnyaguthii.git
cd coffee-shop-pythonnyaguthii
Create and activate a virtual environment
Using pipenv:
pipenv install
pipenv shell
Run the project
You can use the interactive console or run test files:
python debug.py
## Project Structure
coffee-shop-pythonnyaguthii/
├── Pipfile
├── Pipfile.lock
├── README.md
├── __pycache__/
│   ├── coffee.cpython-312.pyc
│   ├── customer.cpython-312.pyc
│   └── order.cpython-312.pyc
├── coffee.py
├── customer.py
├── debug.py
├── order.py
└── tests/
    ├── coffee_test.py
    ├── customer_test.py
    └── order_test.py
## Usage
 Launch the Console
python debug.py
Use methods like:

customer.orders()

coffee.customers()

order.price

to interact with the system.

## Customization
You can customize:

Validations: Add rules in each class initializer

Relationships: Add methods like most_frequent_customer or average_order_price

Tests: Expand the tests/ directory with additional test cases

## Contributors
Nyaguthii (https://github.com/JENNIFER754-DEL)

### Contributing
Fork the repository

Create a new branch (git checkout -b feature/my-feature)

Commit your changes (git commit -m "Add my feature")

Push to GitHub (git push origin feature/my-feature)

Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Python official documentation

Object-Oriented Design principles

Classic coffee shop ordering workflows