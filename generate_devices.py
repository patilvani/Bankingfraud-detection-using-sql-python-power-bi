import mysql.connector
import random
from faker import Faker

fake = Faker()

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vanisai@6630",
    database="bankingfraud"
)

cursor = conn.cursor()

device_types = [
    "Mobile",
    "Laptop",
    "Desktop",
    "Tablet"
]

operating_systems = [
    "Android",
    "iOS",
    "Windows",
    "macOS",
    "Linux"
]

devices = []

for i in range(15000):

    device_type = random.choice(device_types)

    if device_type == "Mobile":
        os = random.choice(["Android", "iOS"])
    elif device_type in ["Laptop", "Desktop"]:
        os = random.choice(["Windows", "macOS", "Linux"])
    else:
        os = random.choice(["Android", "iOS"])

    ip_address = fake.ipv4_public()

    devices.append(
        (
            device_type,
            os,
            ip_address
        )
    )

query = """
INSERT INTO devices
(device_type, operating_system, ip_address)
VALUES (%s, %s, %s)
"""

cursor.executemany(query, devices)

conn.commit()

print("15000 device records inserted successfully!")

cursor.close()
conn.close()