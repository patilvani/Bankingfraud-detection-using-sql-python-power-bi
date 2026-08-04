import mysql.connector
import random
from datetime import datetime, timedelta

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vanisai@6630",
    database="bankingfraud"
)

cursor = conn.cursor()

# Account types
account_types = ["Savings", "Current", "Salary", "Business"]

# Generate 7000 accounts
accounts = []

for account_id in range(1, 7001):

    # Customer IDs between 1 and 5000
    customer_id = random.randint(1, 5000)

    account_type = random.choice(account_types)

    # Random balance
    balance = round(random.uniform(1000, 500000), 2)

    # Random opening date
    start_date = datetime(2015, 1, 1)
    random_days = random.randint(0, 4000)
    opening_date = start_date + timedelta(days=random_days)

    account_status = random.choice(["Active", "Inactive", "Blocked"])
    accounts.append(
        (
            account_id,
            customer_id,
            account_type,
            balance,
            account_status,
            opening_date.date()
        )
    )


query = """
INSERT INTO accounts
(account_id, customer_id, account_type, balance, account_status, open_date)
VALUES (%s,%s,%s,%s,%s,%s)
"""

cursor.executemany(query, accounts)

conn.commit()

print("7000 account records inserted successfully!")

cursor.close()
conn.close()