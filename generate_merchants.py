import mysql.connector
import random

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vanisai@6630",
    database="bankingfraud"
)

cursor = conn.cursor()

merchant_categories = [
    "Supermarket",
    "Restaurant",
    "Electronics",
    "Pharmacy",
    "Fuel Station",
    "Hospital",
    "Clothing",
    "Travel",
    "Entertainment",
    "E-commerce"
]

cities_states = [
    ("Hyderabad", "Telangana"),
    ("Bengaluru", "Karnataka"),
    ("Chennai", "Tamil Nadu"),
    ("Mumbai", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Pune", "Maharashtra"),
    ("Kolkata", "West Bengal"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Vijayawada", "Andhra Pradesh"),
    ("Ahmedabad", "Gujarat")
]

merchants = []

for i in range(1, 501):
    category = random.choice(merchant_categories)
    city, state = random.choice(cities_states)
    merchant_name = f"{category}_{i}"
    rating = round(random.uniform(3.0, 5.0), 1)

    merchants.append(
        (
            merchant_name,
            category,
            city,
            state,
            rating
        )
    )

query = """
INSERT INTO merchants
(merchant_name, merchant_category, city, state, merchant_rating)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(query, merchants)
conn.commit()

print("500 merchant records inserted successfully!")

cursor.close()
conn.close()