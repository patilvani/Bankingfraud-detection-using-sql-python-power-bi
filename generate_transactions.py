import mysql.connector
import random
from datetime import datetime, timedelta

# ===========================
# MySQL Connection
# ===========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vanisai@6630",
    database="bankingfraud"
)

cursor = conn.cursor()

# ===========================
# Lists
# ===========================

transaction_types = [
    "Purchase",
    "Transfer",
    "ATM Withdrawal",
    "Bill Payment",
    "Deposit"
]

payment_methods = [
    "UPI",
    "Debit Card",
    "Credit Card",
    "Net Banking",
    "Wallet"
]

statuses = [
    "Success",
    "Failed",
    "Pending"
]

transactions = []

# ===========================
# Generate 100000 Transactions
# ===========================

start_date = datetime(2022, 1, 1)

for i in range(100000):

    account_id = random.randint(1, 7000)

    merchant_id = random.randint(1, 500)

    device_id = random.randint(1, 15000)

    location_id = random.randint(1, 20)

    transaction_type = random.choice(transaction_types)

    payment_method = random.choice(payment_methods)

    transaction_time = start_date + timedelta(
        days=random.randint(0, 1500),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    amount = round(random.uniform(100, 200000), 2)

    status = random.choices(
        statuses,
        weights=[90, 5, 5]
    )[0]

    # ===========================
    # Fraud Logic
    # ===========================

    fraud_flag = 0

    if (
        amount > 100000
        or (
            transaction_time.hour >= 1
            and transaction_time.hour <= 4
        )
        or status == "Failed"
    ):
        if random.random() < 0.60:
            fraud_flag = 1

    transactions.append(
        (
            account_id,
            merchant_id,
            device_id,
            location_id,
            amount,
            transaction_type,
            payment_method,
            transaction_time,
            status,
            fraud_flag
        )
    )
    # ===========================
# Insert into MySQL
# ===========================

query = """
INSERT INTO transactions
(
account_id,
merchant_id,
device_id,
location_id,
amount,
transaction_type,
payment_method,
transaction_time,
transcation_status,
fraud_flag
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

cursor.executemany(query, transactions)

conn.commit()

print("100000 transaction records inserted successfully!")

cursor.close()
conn.close()