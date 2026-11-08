# Reflection Question 1:
# I would use .get() when a key might not exist because it prevents
# a KeyError and allows me to provide a default value. I would use
# bracket notation when I know the key should always be present.
# My rule of thumb is to use .get() for optional data and brackets
# for required data.

# Reflection Question 2:
# This pattern reminds me of a PivotTable or summary report in Excel
# because it groups and totals data. The Python version is more useful
# for large datasets because it can automatically process thousands of
# records with loops and calculations.

# Exercise 1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2

customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), only the keys are returned.
for key in customer:
    print(key)

    # Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

purchase_amount = 200

discount_rate = tier_discounts.get(customer["tier"], 0)

discount = purchase_amount * discount_rate

final_price = purchase_amount - discount

print("Tier:", customer["tier"])
print("Discount Rate:", discount_rate)
print("Final Price:", final_price)

# Exercise 6

customers = [
    {"name": "Alice", "tier": "gold", "ytd_spend": 12400},
    {"name": "Bob", "tier": "silver", "ytd_spend": 7500},
    {"name": "Charlie", "tier": "platinum", "ytd_spend": 22000}
]

for customer in customers:
    discount_rate = tier_discounts.get(customer["tier"], 0)
    discount_amount = 300 * discount_rate

    print(
        customer["name"],
        customer["tier"],
        discount_amount
    )

# Exercise 7

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print("LOW STOCK:", product)

# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(region, summary[region])
