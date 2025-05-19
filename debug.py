from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.5)
alice.create_order(espresso, 4.0)
bob.create_order(latte, 5.0)

print(alice.orders())
print([c.name for c in alice.coffees()])
print([c.name for c in latte.customers()])
print(latte.num_orders())
print(latte.average_price())
